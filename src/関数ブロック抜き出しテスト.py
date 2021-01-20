#============================================================================================================================================================
import re
import os
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
#============================================================================================================================================================
def testimpl3(filepath):
   breadcrumbs = list()
   breadcrumbs.append(os.path.basename(filepath))
   targetnest = 0
   nest = 0
   maxnest = 0
   buf = ""
   linecnt = 0
   #------------------------------
   #ネスト０の処理
   with open(filepath, "r", encoding="utf-8") as input:
      with open("html/"+breadcrumbs[targetnest]+".html", "w", encoding="utf-8") as output:
         head(output)
         linecnt = 0
         for line in input:
            linecnt+=1
            if line.find("{") != -1:
               nest+=len(re.findall("{", line))
            if line.find("}") != -1:
               nest-=len(re.findall("}", line))
            if nest > maxnest:
               maxnest = nest
            output.write(line)
         body(output)
   #------------------------------
   #ネスト１以上の処理
   targetnest+=1
   while targetnest <= maxnest:
      DrawTargetNest(filepath, targetnest)
      targetnest+=1
#------------------------------
def DrawTargetNest(filepath, targetnest):
   with open(filepath, "r", encoding="utf-8") as input:
      buf = list()
      nest = 0
      linecnt = 0
      for line in input:
         linecnt+=1
         #------------------------------
         #対象ネストより二つ以上上の階層は無視
         if nest < targetnest - 1:
            buf = []
         #対象ネストより一つ上の階層でも空白行は無視
         elif nest == targetnest - 1 and re.fullmatch("\s*", line):
            buf = []
         elif nest == targetnest - 1 and re.fullmatch(".*\}.*\{.*", line, re.S):
            buf = []
         #対象ネストより一つ上の階層もしくは対象ネストより下の階層は保存
         elif nest == targetnest - 1 or nest >= targetnest:
            buf.append([linecnt,line])
         #------------------------------
         if line.find("{") != -1:
            nest+=len(re.findall("{", line))
         if line.find("}") != -1:
            nest-=len(re.findall("}", line))
         #------------------------------
         if re.fullmatch(".*\}.*\{.*", line, re.S):
            #print("skip this line : ",line)
            line = line
         elif line.find("}") != -1:
            if nest == targetnest - 1:
               with open("html/"+os.path.basename(filepath)+"-"+str(targetnest)+"-"+str(buf[0][0])+"-"+str(linecnt)+".html", "w", encoding="utf-8") as output:
                  bufAnalyze(buf)
                  output.write("targetnest is : " + str(targetnest) + "<br>")
                  output.write("startline is : " + str(buf[0][0]) + "<br>")
                  output.write("endline is : " + str(linecnt) + "<br>")
                  output.write("total linecnt is : " + str(len(buf)) + "<br>")
                  head(output)
                  for item in buf:
                     output.write(item[1])
                  body(output)
               buf = []
def bufAnalyze(buf):
   temp = ""
   #------------------------------
   #コメント削除
   for item in buf:
      if re.fullmatch(".*//.*\n", item[1]):
         #print("コメント行なので追加しない", item[1])
         item = item
      elif re.fullmatch("\s*.*:\n", item[1]):
         item = item
      elif re.fullmatch("\s*.*;\n", item[1]):
         item = item
      else:
         temp+=item[1]
      ret = re.fullmatch(".*(\/\*.*\*\/).*", temp, re.S)
      if ret:
         temp = temp.replace(ret.group(1), "")
   #------------------------------
   #{までの空白行削除
   temp2 = ""
   for line in temp.split("\n"):
      if re.fullmatch("\s", line):
         line = line
      else:
         temp2 += line
   #------------------------------
   #(手前を取得
   temp3 = ""
   if re.fullmatch(".*(.*).*{.*}.*", temp2):
      temp3 = temp2[:temp2.find("{")+1]
      print("=================================")
      #print(temp2)
      #print("---------------------------------")
      print(temp3)
   #else:
   #   temp3 = temp2[:temp2.find("{")+1]
   #   print(temp2)
   
def head(io):
   io.write('<!-------------------------------------------------------------------------------!>\n')
   io.write('<html lang="ja">\n')
   io.write('<head>\n')
   io.write('<meta charset="UTF-8">\n')
   io.write('<!--\n')
   io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreDjango.css"/>\n')
   io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreEclipse.css"/>\n')
   io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreFadeToGrey.css"/>\n')
   io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreFadeToGrey.css"/>\n')
   io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreMDUltra.css"/>\n')
   io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreMidnight.css"/>\n')
   io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreRDark.css"/>\n')
   io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreDefault.css"/>\n')
   io.write('!-->\n')
   io.write('<link rel="stylesheet" type="text/css" href="styles/shCoreDjango.css"/>\n')
   io.write('<script type="text/javascript" src="scripts/shCore.js"></script>\n')
   io.write('<script type="text/javascript" src="scripts/shBrushCpp.js"></script>\n')
   io.write('<script type="text/javascript">SyntaxHighlighter.all();</script>\n')
   io.write('<title>XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</title>\n')
   io.write('</head>\n')
   io.write('<body>\n')
   io.write('<a href="AAA">AAA</a> > <a href="BBB">BBB</a> > <a href="CCC">CCC</a>\n')
   io.write('<!-------------------------------------------------------------------------------!>\n')
   io.write('<pre class="brush:cpp">\n')
def body(io):
   io.write('</pre>\n')
   io.write('<!-------------------------------------------------------------------------------!>\n')
   io.write('</body>\n')
   io.write('</html>\n')
   io.write('<!-------------------------------------------------------------------------------!>\n')
#============================================================================================================================================================
if __name__ == '__main__':
   testimpl3("target.cpp")
   #DrawTargetNest("target.cpp", 1)
#============================================================================================================================================================
