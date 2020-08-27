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
  
### 部署命令
- docker build -t fastapi .
- docker run -d --name mycontainer -v $(pwd):/app -p  $(port):80 fastapi
  - Example：  
    docker run -d --name fastapi-platform -v /home/FastApiSkeleton/app:/app -p  8000:80 fastapi