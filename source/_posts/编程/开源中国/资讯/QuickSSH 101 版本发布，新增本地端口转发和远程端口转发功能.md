
---
title: 'QuickSSH 1.0.1 版本发布，新增本地端口转发和远程端口转发功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7061'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 10:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7061'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px">QuickSSH1.0.1版本更新，本次更新新增SSH协议的本地端口转发和远程端口转发功能，具体功能描述推荐参阅阮一峰的文章<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2011%2F12%2Fssh_port_forwarding.html" target="_blank">SSH原理与运用（二）：远程操作与端口转发</a>。</p> 
<p style="margin-left:0px; margin-right:0px">更新功能使用实例</p> 
<pre><code class="language-java">//1.0.1版本新增本地端口转发和远程端口转发
LocalForwardChannel localForwardChannel = sshClient.localForwardChannel();
//访问本机9999端口，系统会将发往9999端口的数据转发到服务器的80端口
localForwardChannel.localForward(9999,"0.0.0.0",80);

RemoteForwardChannel remoteForwardChannel = sshClient.remoteForwardChannel();
//访问远程机器的本机10000端口，系统会将数据转发到本机的80端口
remoteForwardChannel.remoteForward(10000,"127.0.0.1",80);
System.out.println("请在远程机器本地(127.0.0.1)访问10000端口,该请求会转发至本机的80端口!");</code></pre> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span>QuickSSH</span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>纯Java实现SSH协议</span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span>快速入门</span></h1> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>导入QuickSSH</span></li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>cn.schoolwow<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>QuickSSH<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">version</span>></span>&#123;最新版本&#125;<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsearch.maven.org%2Fsearch%3Fq%3Da%3AQuickSSH" target="_blank"><span>QuickSSH最新版本查询</span></a></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>构建SSHClient</span></li> 
</ul> 
<pre><code class="language-java">//密码方式登录
SSHClient client = QuickSSH.newInstance()
        .host("127.0.0.1")
        .port(22)
        .username("root")
        .password("123456")
        .build();
//公钥文件方式登录
SSHClient client = QuickSSH.newInstance()
        .host("127.0.0.1")
        .port(22)
        .username("root")
        //目前仅支持rsa类型
        .publickey("/path/to/id_rsa", "passphrase")
        .build();
//执行exec命令
String resut = sshClient.exec("pwd");
//获取sftp命令
SFTPChannel sftpChannel = sshClient.sftp();
sftpChannel.xxxxxx();</code></pre> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span>开源协议</span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>本软件使用</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.gnu.org%2Flicenses%2Flgpl-3.0-standalone.html" target="_blank"><span>LGPL</span></a><span>开源协议!</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">衷心希望我们国家的开源事业蓬勃发展，也希望大家能重视底层开发。再好的空中楼阁也终究会坍塌，一步一个脚印才能走的更稳，有些捷径是走不得的。共勉。</p>
                                        </div>
                                      
</div>
            