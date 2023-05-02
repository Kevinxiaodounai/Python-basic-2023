import io
import subprocess
import pprint


def system_cmd(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
    proc.wait()
    stream_stdout = io.TextIOWrapper(proc.stdout)
    stream_stderr = io.TextIOWrapper(proc.stderr)

    str_stout = str(stream_stdout.read())
    str_stderr = str(stream_stderr.read())

    return str_stout, str_stderr
#成功是str_stout ，失败是 str_stderr

if __name__ == '__main__':
    exec_cmd = 'ifconfig'

    print(system_cmd(exec_cmd))
    # pprint.pprint(system_cmd(exec_cmd))
