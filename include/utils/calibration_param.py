from typing import List, Dict, Set
import copy
import os
import json

import numpy
import scipy.spatial.transform


class Rotation:
    """旋转，用于旋转矩阵、欧拉角、四元数之间的相互转换

    Returns:
        Rotation: 旋转
    """

    data: List[float]

    def __init__(self, data: List[float] = []):
        """构造Rotation

        Args:
            data (List[float]): 旋转矩阵列表，列表包含旋转矩阵的9个值
        """
        if len(data):
            self.data = copy.deepcopy(data)
        else:
            self.data = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]

    @classmethod
    def fromMatrix(cls, matrix: List[List[float]]):
        """从旋转矩阵构造Rotation

        Args:
            matrix (List[List[float]]): 3*3的旋转矩阵

        Returns:
            Rotation: Rotation
        """
        return Rotation(
            [
                matrix[0][0],
                matrix[0][1],
                matrix[0][2],
                matrix[1][0],
                matrix[1][1],
                matrix[1][2],
                matrix[2][0],
                matrix[2][1],
                matrix[2][2],
            ]
        )

    @classmethod
    def fromEular(
        cls,
        roll: float,
        pitch: float,
        yaw: float,
        degrees: bool = False,
        seq: str = "XYZ",
    ):
        """从欧拉角构造Rotation

        Args:
            roll (float): 翻滚角，即绕X轴的旋转
            pitch (float): 俯仰角，即绕Y轴的旋转
            yaw (float): 偏航角，即绕Z轴的旋转
            degrees (bool, optional): 是否使用角度制
            seq (str, optional): 欧拉角的内外旋和顺序

        Returns:
            Rotation: Rotation
        """
        matrix = scipy.spatial.transform.Rotation.from_euler(
            seq, (roll, pitch, yaw), degrees
        ).as_matrix()
        return cls.fromMatrix(matrix)

    @classmethod
    def fromQuat(cls, w: float, x: float, y: float, z: float):
        """从四元数构造Rotation

        Args:
            w (float): w
            x (float): x
            y (float): y
            z (float): z

        Returns:
            Rotation: Rotation
        """
        matrix = scipy.spatial.transform.Rotation.from_quat([x, y, z, w]).as_matrix()
        return cls.fromMatrix(matrix)

    def getMatrix(self) -> List[List[float]]:
        """获取旋转矩阵形式的Rotation

        Returns:
            List[List[float]]: 旋转矩阵
        """
        return [
            [self.data[0], self.data[1], self.data[2]],
            [self.data[3], self.data[4], self.data[5]],
            [self.data[6], self.data[7], self.data[8]],
        ]

    def getEular(self, seq: str = "XYZ", degrees: bool = False) -> List[float]:
        """获取欧拉角形式的Rotation

        Args:
            seq (str, optional): 欧拉角的内外旋和顺序
            degrees (bool, optional): 是否使用角度制

        Returns:
            List[float]: 欧拉角
        """
        eular = scipy.spatial.transform.Rotation.from_matrix(self.getMatrix()).as_euler(
            seq, degrees
        )
        return [eular[0], eular[1], eular[2]]

    def getQuat(self) -> List[float]:
        """获取四元数形式的Rotation

        Returns:
            List[float]: 四元数，顺序为w、x、y、z
        """
        quat = scipy.spatial.transform.Rotation.from_matrix(self.getMatrix()).as_quat()
        return [quat[3], quat[0], quat[1], quat[2]]


class CalibrationParam:
    """标定参数

    Returns:
        CalibrationParam: 标定参数
    """

    name: str
    target: str
    rotation: Rotation
    translation: List[float]

    channel: str
    modality: str

    image_size: List[int]
    intrinsic: List[float]
    distortion: List[float]
    undistort_intrinsic: List[float]
    undistort_distortion: List[float]

    def __init__(self, calibration_param_path: str = "") -> None:
        """读取标定参数json文件构造标定参数，如果路径为空字符串，则只会初始化标定参数

        Args:
            calibration_param_path (str, optional): 标定参数文件路径
        """
        self.name = ""
        self.target = ""
        self.rotation = Rotation()
        self.translation = []
        self.channel = ""
        self.modality = ""
        self.image_size = []
        self.intrinsic = []
        self.distortion = []
        self.undistort_intrinsic = []
        self.undistort_distortion = []
        if calibration_param_path == "":
            return
        with open(calibration_param_path) as calibration_param_json:
            calibration_param: Dict = json.load(calibration_param_json)
        self.name = os.path.splitext(os.path.basename(calibration_param_path))[0]
        self.target = calibration_param["target"]
        self.rotation = Rotation(calibration_param["rotation"])
        self.translation = calibration_param["translation"]
        self.channel = calibration_param["channel"]
        self.modality = calibration_param["modality"]
        self.image_size = calibration_param["image_size"]
        self.intrinsic = calibration_param["intrinsic"]
        self.distortion = calibration_param["distortion"]
        self.undistort_intrinsic = calibration_param["undistort_intrinsic"]
        self.undistort_distortion = calibration_param["undistort_distortion"]

    def __str__(self) -> str:
        return (
            f"name:\n'{self.name}',\n\n"
            f"target:\n'{self.target}',\n\n"
            f"extrinsic:\n'{self.getExtrinsic()}',\n\n"
            f"rotation:\n{self.rotation.data},\n\n"
            f"translation:\n{self.translation},\n\n"
            f"channel:\n'{self.channel}',\n\n"
            f"modality:\n'{self.modality}',\n\n"
            f"image_size:\n{self.image_size},\n\n"
            f"intrinsic:\n{self.intrinsic},\n\n"
            f"distortion:\n{self.distortion},\n\n"
            f"undistort_intrinsic:\n{self.undistort_intrinsic},\n\n"
            f"undistort_distortion:\n{self.undistort_distortion}"
        )

    def getExtrinsic(self, inverse: bool = False) -> List[List[float]]:
        """获取标定参数的外参矩阵

        Args:
            inverse (bool, optional): 是否求逆矩阵

        Returns:
            List[List[float]]: 外参矩阵
        """
        extrinsic = numpy.eye(4)
        extrinsic[:3, :3] = numpy.array(self.rotation.getMatrix())
        extrinsic[:3, 3] = numpy.array(self.translation)

        if inverse:
            extrinsic = numpy.linalg.inv(extrinsic)

        return extrinsic.tolist()

    def setExtrinsic(self, extrinsic: List[List[float]]):
        """设置标定参数的外参矩阵，实际上读取外参矩阵的值，设置标定参数的rotation和translation

        Args:
            extrinsic (List[List[float]]): 外参矩阵
        """
        self.rotation = Rotation(
            [
                extrinsic[0][0],
                extrinsic[0][1],
                extrinsic[0][2],
                extrinsic[1][0],
                extrinsic[1][1],
                extrinsic[1][2],
                extrinsic[2][0],
                extrinsic[2][1],
                extrinsic[2][2],
            ]
        )
        self.translation = [extrinsic[0][3], extrinsic[1][3], extrinsic[2][3]]

    def save(self, calibration_param_path: str):
        """保存标定参数到指定路径

        Args:
            calibration_param_path (str): 标定参数文件路径
        """
        calibration_param = {
            "target": self.target,
            "rotation": self.rotation.data,
            "translation": self.translation,
            "channel": self.channel,
            "modality": self.modality,
            "image_size": self.image_size,
            "intrinsic": self.intrinsic,
            "distortion": self.distortion,
            "undistort_intrinsic": self.undistort_intrinsic,
            "undistort_distortion": self.undistort_distortion,
        }
        with open(calibration_param_path, "w") as calibration_param_json:
            json.dump(calibration_param, calibration_param_json, indent=4)


class CalibrationParamCalculator:
    """标定参数计算器，载入多个标定参数，构造标定参数图，通过深度优先遍历查找并计算所需的标定参数

    Raises:
        ValueError: 源标定参数名称不存在
        ValueError: 目标标定参数名称不存在
        RuntimeError: 无法搜索从指定源标定参数名称到目标标定参数名称的标定参数

    Returns:
        CalibrationParamCalculator: 标定参数计算器
    """

    calibration_params: List[CalibrationParam]
    names: Set[str]
    names_dict: Dict[str, int]
    index_dict: Dict[int, str]

    adjacency_matrix: List[List[List[List[float]]]]

    def __init__(self, calibration_params_root_path: str = ""):
        """遍历标定参数根目录，读取标定参数json文件构造标定参数计算器，如果路径为空字符串，则只会初始化标定参数计算器

        Args:
            calibration_params_root_path (str, optional): 标定参数根目录
        """
        self.calibration_params = []
        self.names = set()
        self.names_dict = {}
        self.index_dict = {}
        self.adjacency_matrix = []

        if calibration_params_root_path == "":
            return
        # 遍历标定参数根目录
        for calibration_param_path in os.listdir(calibration_params_root_path):
            # 读取扩展名为json的文件
            if os.path.splitext(calibration_param_path)[1] != ".json":
                continue
            # 使用标定参数文件路径来构造CalibrationParam对象
            self.loadCalibrationParam(
                CalibrationParam(
                    os.path.join(calibration_params_root_path, calibration_param_path)
                )
            )

    def init(self):
        """根据已有的标定参数，创建邻接矩阵以及标定参数名称与对应索引、索引与对应标定参数名称的字典"""
        self.names_dict = {}
        self.index_dict = {}
        # 创建邻接矩阵
        self.adjacency_matrix = [
            [[] for _ in range(len(self.names))] for _ in range(len(self.names))
        ]
        # 遍历标定参数名称集合，根据标定参数容器的内容，更新邻接矩阵
        for x, name_x in enumerate(self.names):
            self.names_dict.update(
                {name_x: x}
            )  # 将标定参数名称与对应索引添加到有序键值对容器中
            self.index_dict.update(
                {x: name_x}
            )  # 将索引与对应标定参数名称添加到有序键值对容器中
            for y, name_y in enumerate(self.names):
                for calibration_param in self.calibration_params:
                    # 如果遍历到的标定参数名称与目标标定参数名称与标定参数容器中对应的标定参数匹配，则将外参矩阵与外参矩阵的逆矩阵更新到邻接矩阵中
                    if (
                        calibration_param.name == name_x
                        and calibration_param.target == name_y
                    ):
                        self.adjacency_matrix[x][y] = calibration_param.getExtrinsic()
                        self.adjacency_matrix[y][x] = calibration_param.getExtrinsic(
                            True
                        )
                    elif (
                        calibration_param.name == name_y
                        and calibration_param.target == name_x
                    ):
                        self.adjacency_matrix[x][y] = calibration_param.getExtrinsic(
                            True
                        )
                        self.adjacency_matrix[y][x] = calibration_param.getExtrinsic()

    def DFS(self, start: int, end: int) -> List[int]:
        """从指定节点开始深度优先遍历标定参数图，搜索到指定节点结束的路径

        Args:
            start (int): 起始节点索引
            end (int): 结束节点索引

        Returns:
            List[int]: 从起始节点到结束节点的路径，如果路径不存在则为空列表
        """
        visited = [
            False for _ in range(len(self.adjacency_matrix))
        ]  # 记录每个索引对应的节点是否被访问过
        parent = [
            start for _ in range(len(self.adjacency_matrix))
        ]  # 记录每个索引对应的节点的父节点
        nodes: List[int] = []  # 记录待访问的节点的索引
        nodes.append(start)  # 将起始节点入栈
        visited[start] = True  # 将起始节点标记为已访问

        # 当待访问节点栈为空时，则代表不存在从起始节点到结束节点的路径，返回空列表
        while len(nodes):
            current = nodes[-1]  # 从栈顶获取待访问节点作为当前节点
            nodes.pop()  # 当前节点出栈

            # 如果当前节点为结束节点，则返回从起始节点到结束节点的路径
            if current == end:
                path: List[int] = []  # 记录从结束节点到起始节点的路径

                # 如果当前节点为起始节点则停止循环
                while current != start:
                    path.append(current)  # 记录当前节点
                    current = parent[
                        current
                    ]  # 从父节点容器中获取当前节点的父节点作为当前节点
                path.append(start)  # 记录起始节点
                path.reverse()  # 反转记录的路径，以获取从起始节点到结束节点的路径
                return path

            # 如果当前节点不为结束节点，则遍历邻接矩阵查询可用邻居节点
            for index in range(len(self.adjacency_matrix)):
                # 如果邻居节点已被访问过或与当前节点无连接，则跳过该节点
                if visited[index] or not len(self.adjacency_matrix[current][index]):
                    continue
                # 如果邻居节点未被访问过且与当前节点有连接，则将节点入栈，并标记为已访问，同时记录下该邻居节点的父节点为当前节点
                nodes.append(index)  # 将邻居节点入栈
                visited[index] = True  # 将邻居节点标记为已访问
                parent[index] = current  # 记录下邻居节点的父节点为当前节点

        return []

    def loadCalibrationParam(self, calibration_param: CalibrationParam):
        """载入标定参数

        Args:
            calibration_param (CalibrationParam): 标定参数
        """
        self.calibration_params.append(
            copy.deepcopy(calibration_param)
        )  # 将标定参数添加到容器中
        self.names.add(calibration_param.name)  # 将标定参数名称添加到集合中
        self.names.add(calibration_param.target)  # 将标定参数的target名称添加到集合中

    def getExtrinsic(self, source: str, target: str) -> List[List[float]]:
        """根据指定标定参数名称以及目标标定参数名称，返回对应的外参矩阵

        Args:
            source (str): 源标定参数名称
            target (str): 目标标定参数名称

        Raises:
            ValueError: 源标定参数名称不存在
            ValueError: 目标标定参数名称不存在
            RuntimeError: 无法搜索从指定源标定参数名称到目标标定参数名称的标定参数

        Returns:
            List[List[float]]: 外参矩阵
        """
        if len(self.adjacency_matrix) != self.names:
            self.init()
        if source not in self.names:
            raise ValueError("Error source name " + source)
        if target not in self.names:
            raise ValueError("Error target name " + target)

        # 从源标定参数开始深度优先遍历标定参数图，搜索到目标标定参数的路径
        path = self.DFS(self.names_dict[source], self.names_dict[target])

        # 检查路径是否存在
        if not len(path):
            raise RuntimeError(
                "Path does not exist between " + source + " and " + target
            )

        # 按照起始节点到结束节点的路径，计算从源标定参数到目标标定参数的外参矩阵
        extrinsics: List[List[List[float]]] = []
        # 按照路径顺序，将对应外参矩阵入栈，并按照路径顺序打印标定参数名称
        for index in range(len(path) - 1):
            extrinsics.append(self.adjacency_matrix[path[index]][path[index + 1]])
        #     print(self.index_dict[path[index]],"->",end=" ")
        # print(self.index_dict[path[-1]])

        if len(extrinsics):
            extrinsic = extrinsics.pop()  # 从栈顶获取外参矩阵作为初始外参矩阵
        else:
            extrinsic = [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
            ]  # 如果栈为空，则说明路径只包含一个节点，即起始节点就是结束节点，使用单位矩阵作为初始外参矩阵

        # 当待计算外参矩阵栈为空时，则代表从源标定参数到目标标定参数的外参矩阵计算完成，返回计算结果
        while len(extrinsics):
            extrinsic = numpy.matmul(
                numpy.array(extrinsic), numpy.array(extrinsics.pop())
            ).tolist()  # 从栈顶获取外参矩阵并与初始外参矩阵相乘后作为初始外参矩阵

        return extrinsic

    def getCalibrationParam(self, source: str, target: str) -> CalibrationParam:
        """根据指定标定参数名称以及目标标定参数名称、标定参数文件的保存路径，返回对应的标定参数

        Args:
            source (str): 源标定参数名称
            target (str): 目标标定参数名称

        Returns:
            CalibrationParam: 标定参数
        """
        calibration_param = None

        # 查询标定参数容器是否存在源标定参数，如果存在源标定参数，则使用源标定参数构造新的标定参数
        for calibration_param_ in self.calibration_params:
            if calibration_param_.name == source:
                calibration_param = copy.deepcopy(calibration_param_)
                break

        # 如果不存在源标定参数，则直接构造新的标定参数，并设置标定参数名称
        if calibration_param == None:
            calibration_param = CalibrationParam()
            calibration_param.name = source

        calibration_param.target = target  # 设置标定参数目标
        calibration_param.setExtrinsic(
            self.getExtrinsic(source, target)
        )  # 设置标定参数外参矩阵

        return calibration_param
