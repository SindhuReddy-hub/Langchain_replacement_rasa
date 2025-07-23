import subprocess

def list_s3_buckets():
    try:
        result = subprocess.run(['aws', 's3', 'ls'], capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)
