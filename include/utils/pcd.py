from typing import List, Union

import numpy
import numpy.typing

from include.utils.calibration_param import Rotation

try:
    import pcl

    def loadPCD(
        pcd_path: str, as_ndarray: bool = True
    ) -> Union[numpy.typing.NDArray, List[List[float]]]:
        """读取PCD文件

        Args:
            pcd_path (str): PCD文件路径
            as_ndarray (bool, optional): 是否以numpy.ndarray形式返回

        Returns:
            Union[numpy.typing.NDArray, List[List[float]]]: 点云数组或列表
        """
        cloud = pcl.load_XYZI(pcd_path)
        return cloud.to_array() if as_ndarray else cloud.to_list()

    def savePCD(
        point_cloud: Union[numpy.typing.NDArray, List[List[float]]], pcd_path: str
    ) -> None:
        """保存点云到指定PCD文件路径中，点云数组或列表中每个点应包含x、y、z、intensity四个维度

        Args:
            point_cloud (Union[numpy.typing.NDArray, List[List[float]]]): 点云数组或列表
            pcd_path (str): PCD文件路径
        """
        if isinstance(point_cloud, list):
            point_cloud_to_save = [
                point[:4] + [0] * max(0, 4 - len(point)) for point in point_cloud
            ]

        else:
            if point_cloud.shape[1] < 4:
                point_cloud_with_intensity = numpy.zeros((point_cloud.shape[0], 4))
                point_cloud_with_intensity[:, :3] = point_cloud[:, :3]
                point_cloud_to_save = point_cloud_with_intensity
            elif point_cloud.shape[1] > 4:
                point_cloud_to_save = point_cloud[:, :4]
            else:
                point_cloud_to_save = point_cloud

            if point_cloud_to_save.dtype != numpy.float32:
                point_cloud_to_save = point_cloud_to_save.astype(numpy.float32)

        pcl.save(pcl.PointCloud_PointXYZI(point_cloud_to_save), pcd_path)

except:

    def loadPCDFIELDS(pcd_line: str) -> List[str]:
        """读取PCD文件中点云的FIELDS

        Args:
            pcd_line (str): PCD文件的FIELDS文本行字符串

        Returns:
            List[str]: FIELDS列表
        """
        return pcd_line.strip().split(" ")[1:]

    def loadPCDDATA(pcd_lines: List[str], fields: List[str]) -> List[List[float]]:
        """读取PCD文件中点云的DATA

        Args:
            pcd_lines (List[str]): PCD文件的数据文本行字符串
            fields (List[str]): FIELDS列表

        Returns:
            List[List[float]]: 点云列表
        """
        point_cloud: list[list[float]] = list()
        for pcd_line in pcd_lines:
            point_data = pcd_line.strip().split(" ")
            point: list[float] = list()
            for index in range(len(fields)):
                data = point_data[index]
                if fields[index] in ["x", "y", "z", "intensity"]:
                    point.append(float(data))
                elif fields[index] == "rgb":
                    rgb = int(data)
                    b = rgb & 0xFF
                    g = (rgb >> 8) & 0xFF
                    r = (rgb >> 16) & 0xFF
                    map(point.append, [r, g, b])
            point_cloud.append(point)
        return point_cloud

    def loadPCD(
        pcd_path: str, as_ndarray: bool = True
    ) -> Union[numpy.typing.NDArray, List[List[float]]]:
        """读取PCD文件，文件中的DATA字段应为ASCII格式

        Args:
            pcd_path (str): PCD文件路径
            as_ndarray (bool, optional): 是否以numpy.ndarray形式返回

        Returns:
            Union[numpy.typing.NDArray, List[List[float]]]: 点云数组或列表
        """
        with open(pcd_path) as pcd_file:
            pcd_lines: list[str] = pcd_file.readlines()

        for index in range(len(pcd_lines)):
            pcd_line: str = pcd_lines[index]
            if pcd_line.startswith("FIELDS"):
                fields: list[str] = loadPCDFIELDS(pcd_line)
            if pcd_line.startswith("DATA"):
                data_start_index: int = index + 1
                break

        point_cloud: list[list[float]] = loadPCDDATA(
            pcd_lines[data_start_index:], fields
        )

        return numpy.array(point_cloud) if as_ndarray else point_cloud

    def savePCD(
        point_cloud: Union[numpy.typing.NDArray, List[List[float]]], pcd_path: str
    ) -> None:
        """保存点云到指定PCD文件路径中，点云数组或列表中每个点应包含x、y、z、intensity四个维度

        Args:
            point_cloud (numpy.typing.NDArray | List[List[float]]): 点云数组或列表
            pcd_path (str): PCD文件路径
        """
        header = (
            "# .PCD v0.7 - Point Cloud Data file format\nVERSION 0.7\nFIELDS x y z intensity\nSIZE 4 4 4 4\nTYPE F F F F\nCOUNT 1 1 1 1\nWIDTH "
            + str(len(point_cloud))
            + "\nHEIGHT 1\nVIEWPOINT 0 0 0 1 0 0 0\nPOINTS "
            + str(len(point_cloud))
            + "\nDATA ascii\n"
        )
        data = str()
        for point in point_cloud:
            data += str(point[0]) + " "
            data += str(point[1]) + " "
            data += str(point[2]) + " "
            data += str(point[3]) + "\n"
        with open(pcd_path, "w") as pcd_file:
            pcd_file.write(header + data)


def transformPointCloud(
    point_cloud: numpy.typing.NDArray, transform: numpy.typing.NDArray
) -> numpy.typing.NDArray:
    """对点云进行坐标转换

    Args:
        point_cloud (numpy.typing.NDArray): 点云数组
        transform (numpy.typing.NDArray): 转换矩阵

    Returns:
        numpy.typing.NDArray: 转换后的点云数组
    """
    transformed_point_cloud = numpy.array(point_cloud)
    temp_point_cloud = numpy.ones((len(point_cloud), 4))
    temp_point_cloud[:, :3] = transformed_point_cloud[:, :3]
    temp_point_cloud = numpy.matmul(temp_point_cloud, transform.T)
    transformed_point_cloud[:, :3] = temp_point_cloud[:, :3]
    return transformed_point_cloud


def transformPointCloudList(
    point_cloud: List[List[float]],
    rotation: Rotation,
    translation: List[float],
    inverse: bool = False,
) -> List[List[float]]:
    """对点云进行坐标转换

    Args:
        point_cloud (List[List[float]]): 点云列表
        rotation (Rotation): 旋转
        translation (List[float]): 平移
        inverse (bool, optional): 是否求逆矩阵

    Returns:
        List[List[float]]: 转换后的点云列表
    """
    transform = numpy.eye(4)
    transform[:3, :3] = numpy.array(rotation.getMatrix())
    transform[:3, 3] = numpy.array(translation)

    if inverse:
        transform = numpy.linalg.inv(transform)

    return transformPointCloud(numpy.array(point_cloud), transform).tolist()


def PointCloudinBox(
    point_cloud: numpy.typing.NDArray,
    center_x: float,
    center_y: float,
    center_z: float,
    length: float,
    width: float,
    height: float,
    roll: float,
    pitch: float,
    yaw: float,
) -> int:
    """根据点云以及目标框的标注信息计算点云是否位于目标框

    Args:
        point_cloud (numpy.typing.NDArray): 点云数组
        center_x (float): 目标框中心的x坐标
        center_y (float): 目标框中心的y坐标
        center_z (float): 目标框中心的z坐标
        length (float): 目标框的长
        width (float): 目标框的宽
        height (float): 目标框的高
        roll (float): 目标框的翻滚角，即绕X轴的旋转
        pitch (float): 目标框的俯仰角，即绕Y轴的旋转
        yaw (float): 目标框的偏航角，即绕Z轴的旋转

    Returns:
        int: 位于目标框内点的数量
    """
    # 计算边界
    half_length = length / 2
    half_width = width / 2
    half_height = height / 2

    # 计算最大边界
    max_distance = (half_length**2 + half_width**2 + half_height**2) ** 0.5
    max_x = center_x + max_distance
    min_x = center_x - max_distance
    max_y = center_y + max_distance
    min_y = center_y - max_distance
    max_z = center_z + max_distance
    min_z = center_z - max_distance

    # 检查点是否在最大边界内
    inside_x = (point_cloud[:, 0] >= min_x) & (point_cloud[:, 0] <= max_x)

    f_point_cloud = point_cloud[inside_x]

    inside_y = (f_point_cloud[:, 1] >= min_y) & (f_point_cloud[:, 1] <= max_y)

    f_point_cloud = f_point_cloud[inside_y]

    inside_z = (f_point_cloud[:, 2] >= min_z) & (f_point_cloud[:, 2] <= max_z)

    f_point_cloud = f_point_cloud[inside_z]

    # 将最大边界内的点转换到目标框坐标系
    transform = numpy.eye(4)
    transform[:3, :3] = numpy.array(Rotation.fromEular(roll, pitch, yaw).getMatrix())
    transform[:3, 3] = numpy.array([center_x, center_y, center_z])
    transform = numpy.linalg.inv(transform)

    points_to_box = transformPointCloud(f_point_cloud, transform)

    # 检查点是否在边界内
    inside_x = (points_to_box[:, 0] >= -half_length) & (
        points_to_box[:, 0] <= half_length
    )

    points_to_box = points_to_box[inside_x]

    inside_y = (points_to_box[:, 1] >= -half_width) & (
        points_to_box[:, 1] <= half_width
    )

    points_to_box = points_to_box[inside_y]

    inside_z = (points_to_box[:, 2] >= -half_height) & (
        points_to_box[:, 2] <= half_height
    )

    # 计算并返回位于目标框内的点的数量
    num_lidar_pts = numpy.sum(inside_z)
    return int(num_lidar_pts)


def PointCloudinLidarFOV(
    point_cloud: numpy.typing.NDArray,
    horizontal_fov: float = 120.0,
    vertical_fov: float = 25.0,
    transform: numpy.typing.NDArray = numpy.eye(4),
    scale: float = 10.0,
):
    """根据激光雷达视场角以及激光雷达外参计算点云是否位于激光雷达视场范围内

    Args:
        point_cloud (numpy.typing.NDArray): 点云数组
        horizontal_fov (float, optional): 激光雷达水平视场角
        vertical_fov (float, optional): 激光雷达垂直视场角
        transform (numpy.typing.NDArray, optional): 转换矩阵
        scale (float, optional):

    Returns:
        _type_: 激光雷达视场范围内的点云
    """
    view_width = horizontal_fov * scale
    view_height = vertical_fov * scale
    intrinsic = numpy.array(
        [
            [
                view_width / 2 / numpy.tan(horizontal_fov / 2 / 180 * numpy.pi),
                0.0,
                view_width / 2,
            ],
            [
                0.0,
                view_height / 2 / numpy.tan(vertical_fov / 2 / 180 * numpy.pi),
                view_height / 2,
            ],
            [0.0, 0.0, 1.0],
        ]
    )
    extrinsic = numpy.matmul(
        numpy.array(
            [
                [0.0, -1.0, 0.0, 0.0],
                [0.0, 0.0, -1.0, 0.0],
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
            ]
        ),
        transform,
    )
    points_to_lidar_view = transformPointCloud(point_cloud, extrinsic)
    points_to_view = numpy.matmul(points_to_lidar_view[:, :3], intrinsic.T)
    points_to_view[:, :2] /= points_to_view[:, 2][:, numpy.newaxis]

    valid = (
        (points_to_view[:, 2] > 0)
        & (points_to_view[:, 0] >= 0)
        & (points_to_view[:, 0] < view_width)
        & (points_to_view[:, 1] >= 0)
        & (points_to_view[:, 1] < view_height)
    )

    return point_cloud[valid]


# def points_in_box(
#     points: List[List[float]],
#     center_x: float,
#     center_y: float,
#     center_z: float,
#     length: float,
#     width: float,
#     height: float,
#     roll: float,
#     pitch: float,
#     yaw: float,
# ) -> int:
#     """根据点云以及目标框的标注信息计算点是否位于目标框

#     Args:
#         points (List[List[float]]): 点云列表
#         center_x (float): 目标框中心的x坐标
#         center_y (float): 目标框中心的y坐标
#         center_z (float): 目标框中心的z坐标
#         length (float): 目标框的长
#         width (float): 目标框的宽
#         height (float): 目标框的高
#         roll (float): 目标框的翻滚角，即绕X轴的旋转
#         pitch (float): 目标框的俯仰角，即绕Y轴的旋转
#         yaw (float): 目标框的偏航角，即绕Z轴的旋转

#     Returns:
#         int: 位于目标框内点的数量
#     """

#     transform = numpy.eye(4)
#     transform[:3, :3] = numpy.array(Rotation.fromEular(roll, pitch, yaw).getMatrix())
#     transform[:3, 3] = numpy.array([center_x, center_y, center_z])
#     transform = numpy.linalg.inv(transform)

#     # 将点云转换到目标框坐标系
#     points_to_box = transformPointCloud(numpy.array(points), transform)

#     # 计算边界
#     half_length = length / 2
#     half_width = width / 2
#     half_height = height / 2

#     # 检查点是否在边界内
#     inside_x = (points_to_box[:, 0] > -half_length) & (
#         points_to_box[:, 0] < half_length
#     )
#     inside_y = (points_to_box[:, 1] > -half_width) & (points_to_box[:, 1] < half_width)
#     inside_z = (points_to_box[:, 2] > -half_height) & (
#         points_to_box[:, 2] < half_height
#     )

#     # 计算并返回位于目标框内的点的数量
#     num_lidar_pts = numpy.sum(inside_x & inside_y & inside_z)
#     return int(num_lidar_pts)
