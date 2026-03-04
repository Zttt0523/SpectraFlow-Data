from handler.run_monitoring_service import run_monitoring_service
import os

if __name__ == '__main__':
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建 config.json 的绝对路径
    config_path = os.path.join(current_dir, "config.json")
    print(f"USING CONFIG: {config_path}")
    # 运行监控服务
    run_monitoring_service(config_path)
