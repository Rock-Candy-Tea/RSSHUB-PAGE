
---
title: 'QuickSSH 1.0.2 版本发布， 支持是否活跃检测功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9051'
author: 开源中国
comments: false
date: Fri, 04 Mar 2022 16:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9051'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">QuickSSH 1.0.2版本发布，新增isClosed方法，用于检测当前会话是否关闭。此方法适用于连接池场景，需要将SSHClient作为资源存储，需要检测SSHClient是否可用。同时新增Channel类可获取所属的SSHClient方法.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更新功能使用实例</p> 
<pre><code class="language-java">SSHClient sshClient =QuickSSH.newInstance()
        .host(account.host())
        .port(account.port())
        .username(account.username())
        .password(account.password())
        .build();
//判断连接是否关闭
sshClient.isClosed();

SFTPChannel sftpChannel = sshClient.sftpChannel();
//获得该频道所属的SSHClient
SSHClient sshClient1 = sftpChannel.getSSHClient();</code></pre> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span>QuickSSH</span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>纯Java实现SSH协议</span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span>快速入门</span></h1> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>导入QuickSSH</span></li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-xml"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span></span>
  <span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span></span>cn.schoolwow<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span></span>
  <span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span>QuickSSH<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span></span>
  <span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span></span>&#123;最新版本&#125;<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span></span>
<span style="color:#333333"><span style="color:#333333"></</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsearch.maven.org%2Fsearch%3Fq%3Da%3AQuickSSH" target="_blank"><span>QuickSSH最新版本查询</span></a></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>构建SSHClient</span></li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d">//密码方式登录</span>
SSHClient client = QuickSSH.newInstance()
        .host(<span style="color:#032f62">"127.0.0.1"</span>)
        .port(<span>22</span>)
        .username(<span style="color:#032f62">"root"</span>)
        .password(<span style="color:#032f62">"123456"</span>)
        .build();
<span style="color:#6a737d">//公钥文件方式登录</span>
SSHClient client = QuickSSH.newInstance()
        .host(<span style="color:#032f62">"127.0.0.1"</span>)
        .port(<span>22</span>)
        .username(<span style="color:#032f62">"root"</span>)
        <span style="color:#6a737d">//目前仅支持rsa类型</span>
        .publickey(<span style="color:#032f62">"/path/to/id_rsa"</span>, <span style="color:#032f62">"passphrase"</span>)
        .build();
<span style="color:#6a737d">//执行exec命令</span>
<span>String</span> resut = sshClient.exec(<span style="color:#032f62">"pwd"</span>);
<span style="color:#6a737d">//获取sftp命令</span>
SFTPChannel sftpChannel = sshClient.sftp();
sftpChannel.xxxxxx();</code></pre> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span>开源协议</span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>本软件使用</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.gnu.org%2Flicenses%2Flgpl-3.0-standalone.html" target="_blank"><span>LGPL</span></a><span>开源协议!</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">衷心希望我们国家的开源事业蓬勃发展，也希望大家能重视底层开发。再好的空中楼阁也终究会坍塌，一步一个脚印才能走的更稳，有些捷径是走不得的。共勉。</p>
                                        </div>
                                      
</div>
            