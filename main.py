import argparse,subprocess
def audit(root):
 rows=subprocess.run(["git","-C",root,"ls-files","-z"],capture_output=True,text=True,check=True).stdout.split("\\0")
 return [x for x in rows if x and subprocess.run(["git","-C",root,"check-ignore","-q","--no-index","--",x]).returncode==0]
def main():
 p=argparse.ArgumentParser();p.add_argument("directory",nargs="?",default=".");a=p.parse_args()
 for x in audit(a.directory):print(x)
if __name__=="__main__":main()