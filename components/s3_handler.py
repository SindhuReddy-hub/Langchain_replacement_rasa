import subprocess

def upload_file_to_s3(file_path, bucket_name):
    try:
        result = subprocess.run(
            ["aws", "s3", "cp", file_path, f"s3://{bucket_name}/"],
            capture_output=True,
            text=True
        )
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)
