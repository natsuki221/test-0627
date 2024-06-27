import cpuinfo
import GPUtil

def get_cpu_info():
    info = cpuinfo.get_cpu_info()
    return info['brand_raw']

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_info = []
    for gpu in gpus:
        gpu_info.append((gpu.name, gpu.driver))
    return gpu_info

if __name__ == "__main__":
    cpu_model = get_cpu_info()
    print(f"CPU 型號: {cpu_model}")

    gpu_models = get_gpu_info()
    if not gpu_models:
        print("未檢測到GPU")
    else:
        for i, (model, driver) in enumerate(gpu_models, start=1):
            print(f"GPU {i} 型號: {model}, 驅動: {driver}")

