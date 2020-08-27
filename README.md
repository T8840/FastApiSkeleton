# FastApiSkeleton
FastApi 项目模板



### Development
#### 命令行启动
uvicorn main:app --reload

#### 数据库迁移
1.清除app/alembic/versons目录下的python文件  
2.初始化命令：alembic revision --autogenerate -m 'init'  
3.提交model变更命令：  
  alembic revision --autogenerate -m '提交说明'  
  alembic upgrade head