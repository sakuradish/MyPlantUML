#============================================================================================================================================================
import re
import os
from memory_profiler import profile
import glob
from MyLogger import mylogger
mylogger = mylogger.GetInstance('DEBUG')
#============================================================================================================================================================
def dprint(*args):
   temp = ""
   for arg in args:
      temp += str(arg)
      temp += " "
   temp = temp.replace("\t", "\\t")
   temp = temp.replace("\n", "\\n")
   temp = temp.replace("\r", "\\r")
   temp = temp.replace("\"", "\\\"")
   print(temp)
# #============================================================================================================================================================
# def testimpl3(filepath):

# #------------------------------
# def DrawTargetNest(filepath, targetnest):

# def bufAnalyze(buf):

#    #------------------------------
#    #{までの空白行削除
#    temp2 = ""
#    for line in temp.split("\n"):
#       if re.fullmatch("\s", line):
#          line = line
#       else:
#          temp2 += line
#    #------------------------------
#    #(手前を取得
#    temp3 = ""
#    if re.fullmatch(".*(.*).*{.*}.*", temp2):
#       temp3 = temp2[:temp2.find("{")+1]
#       print("=================================")
#       #print(temp2)
#       #print("---------------------------------")
#       print(temp3)
#    #else:
#    #   temp3 = temp2[:temp2.find("{")+1]
#    #   print(temp2)
   
# def head(io):
#    io.write('<!-------------------------------------------------------------------------------!>\n')
#    io.write('<html lang="ja">\n')
#    io.write('<head>\n')
#    io.write('<meta charset="UTF-8">\n')
#    io.write('<!--\n')
#    io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreDjango.css"/>\n')
#    io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreEclipse.css"/>\n')
#    io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreFadeToGrey.css"/>\n')
#    io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreFadeToGrey.css"/>\n')
#    io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreMDUltra.css"/>\n')
#    io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreMidnight.css"/>\n')
#    io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreRDark.css"/>\n')
#    io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreDefault.css"/>\n')
#    io.write('!-->\n')
#    io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreDjango.css"/>\n')
#    io.write('<script type="text/javascript" src="scripts/shCore.js"></script>\n')
#    io.write('<script type="text/javascript" src="scripts/shBrushCpp.js"></script>\n')
#    io.write('<script type="text/javascript">SyntaxHighlighter.all();</script>\n')
#    io.write('<title>XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</title>\n')
#    io.write('</head>\n')
#    io.write('<body>\n')
#    io.write('<a href="AAA">AAA</a> > <a href="BBB">BBB</a> > <a href="CCC">CCC</a>\n')
#    io.write('<!-------------------------------------------------------------------------------!>\n')
#    io.write('<pre class="brush:cpp">\n')
# def body(io):
#    io.write('</pre>\n')
#    io.write('<!-------------------------------------------------------------------------------!>\n')
#    io.write('</body>\n')
#    io.write('</html>\n')
#    io.write('<!-------------------------------------------------------------------------------!>\n')
#============================================================================================================================================================
# @profile
@mylogger.deco
def RemoveComment(input, output):
   #コメント削除
   with open(input, "r", encoding="utf-8") as input:
      input = input.readlines()
   with open(output, "w", encoding="utf-8") as output:
      buf = ""
      for line in input:
         buf += line
         #=============================================
         result = re.fullmatch(".*(//.*)\n.*", buf, re.S)
         if result:
            buf = buf.replace(result.group(1), "")
         #=============================================
         result = re.fullmatch(".*(\/\*.*\*\/).*", buf, re.S)
         if result:
            buf = buf.replace(result.group(1), "")
         #=============================================
      output.write(buf)
#============================================================================================================================================================
# @profile
# def TokenizeTest(input,output):
#    #コメント削除
#    with open(input, "r", encoding="utf-8") as input:
#       input = input.readlines()
#    with open(output, "w", encoding="utf-8") as output:
#       buf = ""
#       tokens = []
#       for line in input:
#          for char in line:
#             buf += char
#             # print(buf)
#             # print(re.fullmatch("([a-zA-Z0-9_]*)[^a-zA-Z0-9_]", "test ", re.S))
   
#             result = re.fullmatch("([a-zA-Z0-9_]*).*[^a-zA-Z0-9_]", buf, re.S)
#             if result:
#                tokens.append(result.group(1))
#                buf = buf.replace(result.group(1), "")
#             result = re.fullmatch("[^a-zA-Z0-9_]", buf, re.S)
#             if result:
#                buf = ""
#       print(tokens)
#          # buf += line
#          # #=============================================
#          # result = re.fullmatch(".*(//.*)\n.*", buf, re.S)
#          # if result:
#          #    buf = buf.replace(result.group(1), "")
#          # #=============================================
#          # result = re.fullmatch(".*(\/\*.*\*\/).*", buf, re.S)
#          # if result:
#          #    buf = buf.replace(result.group(1), "")
#          # #=============================================
#       output.write(buf)
#============================================================================================================================================================
# @profile
@mylogger.deco
def CreateFolder(base):
   base = base.replace("/", "\\")
   if os.path.exists(base) and os.path.isdir(base):
      basedirs = [base]
      while 1:
         if not basedirs:
            break
         else:
            basedir = basedirs.pop(0)
         try:
            files = [file for file in glob.glob(basedir + "/*", recursive=False) if os.path.isfile(file)]
            dirs = [dir for dir in glob.glob(basedir + "/*", recursive=False) if os.path.isdir(dir)]
            basedirs += dirs
            for file in files:
               if file.find(".cpp") != -1:
                  file = file.replace(base, "")
                  # print("["+str(len(basedirs))+"]"+file)
                  if not os.path.exists("../out/"+file+"/"):
                     os.makedirs("../out/"+file+"/")
         except:
            print(basedir+" can not glob for some error")
#============================================================================================================================================================
# @profile
@mylogger.deco
def GetBlockList(input):
   with open(input, "r", encoding="utf-8") as input:
      input = input.readlines()
   maxnest = 1
   targetnest = 1
   blocklist = []
   while targetnest <= maxnest:
      nest = 0
      buf = ""
      linecnt = 0
      startline = linecnt
      for line in input:
         linecnt += 1
         #------------------------------
         # {}をカウント
         # method(){return 0;}みたいな一行関数も対応必要一旦保留
         if line.find("{") != -1:
            nest+=len(re.findall("{", line))
            maxnest = nest if nest > maxnest else maxnest
         if line.find("}") != -1:
            nest-=len(re.findall("}", line))
         #------------------------------
         #対象ネストより一つ上の階層でも空白行は無視
         if nest < targetnest - 1:
            buf = ""
         elif nest == targetnest - 1:
            if re.fullmatch("\s*\n", line):
               buf = ""
            elif line.find("{") != -1:
               buf = ""
            elif re.fullmatch("\s*.*:\s*\n", line):
               buf = ""
            elif re.fullmatch("\s*.*;\s*\n", line):
               buf = ""
            else:
               buf+=line
         # elif nest == targetnest - 1 and re.fullmatch(".*\}.*\{.*", line, re.S):
         #    buf = []
         #対象ネストより一つ上の階層もしくは対象ネストより下の階層は保存
         elif nest >= targetnest:
            buf+=line
         #------------------------------
         if line.find("}") != -1 and nest == targetnest - 1:
            blocklist.append({'nest':targetnest, 'start':startline, 'end':linecnt, 'text':buf})
            # buf = ""
         elif line.find("{") != -1 and nest == targetnest:
            startline = linecnt
      targetnest += 1
   # Add Type to each block
   for block in blocklist:
      text = block['text']
      # with open("debug.txt", "a", encoding='utf-8') as temp:
      #    temp.write("========================\n")
      #    temp.write(text)
      print("========================\n")
      print(text)
      result = re.fullmatch("([^\n{]*;[^\n{]*\n).*", text, re.S)
      if result:
         text = text.replace(result.group(1), "")
      text = text.lstrip()
      text = text[:text.find("{")]
      # print(text)
      if re.fullmatch("for.*", text):
         # print("  is for")
         block['type'] = "for"
      elif re.fullmatch("if.*", text):
         # print("  is if")
         block['type'] = "if"
      elif re.fullmatch("class.*", text):
         # print("  is class")
         block['type'] = "class"
      elif re.fullmatch("\s*", text):
         # print("  is simple-block")
         block['type'] = "simple-block"
      else:
         # 別のパターンもありそうだけど保留
         # print("  is function")
         block['type'] = "function"
   return blocklist
#============================================================================================================================================================
# @profile
@mylogger.deco
def GetFunctionList(input):
   RemoveComment(input, "temp.text")
   blocklist = GetBlockList("temp.text")
   with open("temp2.txt", "w") as f:
      # for block in [block for block in blocklist if block['type'] == "function"]:
      for block in [block for block in blocklist]:
         f.write("========================================\n")
         f.write(str(block['nest']) + "\t")
         f.write(str(block['start']) + "\t")
         f.write(str(block['end']) + "\t")
         f.write(str(block['type']) + "\n")
         for text in block['text'].split("\n"):
            f.write(text + "\n")
   return [block for block in blocklist if block['type'] == "function"]
   # with open(output, "w", encoding="utf-8") as output:
#============================================================================================================================================================
# @profile
@mylogger.deco
def DraftUML(base):
   base = base.replace("/", "\\")
   if os.path.exists(base) and os.path.isdir(base):
      basedirs = [base]
      with open("temp.txt", "w", encoding='utf-8') as f:
         while 1:
            if not basedirs:
               break
            else:
               basedir = basedirs.pop(0)
            # try:
            if 1:
               files = [file for file in glob.glob(basedir + "/*", recursive=False) if os.path.isfile(file)]
               dirs = [dir for dir in glob.glob(basedir + "/*", recursive=False) if os.path.isdir(dir)]
               basedirs += dirs
               for file in files:
                  if file.find(".cpp") != -1:
                        f.write(file + "\n")
                  # blocklist = GetFunctionList(file)
                  # dir = file.replace(base, "../out/") + "/"
                  # for block in blocklist:
                  #    text = block['text']
                  #    result = re.fullmatch("([^\n{]*;[^\n{]*\n).*", text, re.S)
                  #    if result:
                  #       text = text.replace(result.group(1), "")
                  #    text = text.lstrip()
                  #    text = text[:text.find("{")]
                  #    result = re.fullmatch(".* (.*)\(.*", text, re.S)
                  #    if result:
                  #       text = result.group(1)
                  #    text = text.replace(":","")
                  #    try:
                  #       with open(dir+text+".pu", "w", encoding='utf-8') as output:
                  #       # with open("temp.pu", "w", encoding='utf-8') as output:
                  #          # print(block['text'])
                  #          output.write(block['text'])
                  #       # print("success " + dir+text+".pu")
                  #    except:
                  #       # print("failed " + dir+text+".pu")
                  #       pass
#============================================================================================================================================================
@mylogger.deco
def main(input):
   # CreateFolder(input)
   DraftUML(input)
def test():
   input = "target.cpp"
   # blocklist = GetBlockList(input)
   blocklist = GetFunctionList(input)
   # for block in blocklist:
   #    print("=================")
   #    print(block['text'])
   # TokenizeTest(input, input+"2")
#============================================================================================================================================================
if __name__ == '__main__':
   # main(r"../data/")
   test()
   #DrawTargetNest("target.cpp", 1)
#============================================================================================================================================================
