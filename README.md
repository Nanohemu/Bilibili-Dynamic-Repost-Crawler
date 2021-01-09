# Bilibili-Dynamic-Repost-Crawler

## 基于b站api的转发动态名单生成

环境：python 3


操作：

1. 复制目标动态的id 赋值给dynamic_id

	>例：  
	>&nbsp;&nbsp;&nbsp;&nbsp;https://t.bilibili.com/408799797598853973?tab=2 的id是 _408799797598853973_  
	>&nbsp;&nbsp;&nbsp;&nbsp;则修改第7行代码为 `dynamic_id = '408799797598853973'` id两端加引号

2. 运行程序 `python get_user_list.py`

3. 程序自动在文件夹下生成 _repo.csv_ 可以使用Excel打开

| | Num | Time | UID | Name |
|:----:|:----:|:----:|:----:|:----:|
| |12|1608389030|32963747|Nanohemu|
| _注解：_ | 第12个转发 | 转发的时间戳 | 用户UID | 用户名 |

附：[时间戳转换工具](https://tool.lu/timestamp/)

**注意：**  
1. b站api只能获取**最新转发的500条动态** 超过后无法获取500条之前的动态  
2. 程序已经过滤了重复转发 但**不能**过滤未关注人和抽奖号  
3. 用户名显示错误和乱码时 将这一列数据格式改成`文本` 并另存为`.xlsx`文件
