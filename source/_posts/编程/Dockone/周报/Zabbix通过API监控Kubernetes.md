
---
title: 'Zabbix通过API监控Kubernetes'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/c1ed241c29af6f0f1c171981e53f8589.png'
author: Dockone
comments: false
date: 2021-04-24 04:09:56
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/c1ed241c29af6f0f1c171981e53f8589.png'
---

<div>   
<br>监控方式：Python+Zabbix_sender<br>
<br>原理：Python的request库，请求Kubernetes的API地址，对数据处理。<br>
<h3>第一步：获取Kubernetes的API地址</h3>查看Kubernetes的API地址的命令如下（最好在Kubernetes集群的master上执行这条命令，因为如果在Node节点上执行该命令有可能会获取旧的API地址）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/c1ed241c29af6f0f1c171981e53f8589.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/c1ed241c29af6f0f1c171981e53f8589.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>第二步：Kubernetes集群的Master主机生成一个Token用来认证，请求数据API数据</h3>生成令牌命令如下（在Kubernetes的Master主机执行命令）：<br>
<pre class="prettyprint">kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep admin-user | awk '&#123;print $1&#125;')<br>
</pre><br>
把Token的值保存在本地的一个文件即可，后期需要把Token值添加到脚本中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/031c5ee29b6bdfabcc61c7b31cf32e52.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/031c5ee29b6bdfabcc61c7b31cf32e52.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
模板脚本下载地址：<br>
<br>链接：<a href="https://pan.baidu.com/s/1zIBudV8pI4peaQ21_sgPMg" rel="nofollow" target="_blank">https://pan.baidu.com/s/1zIBudV8pI4peaQ21_sgPMg</a><br>
<br>提取码：gt8i<br>
<h3>第三步：上传脚本并修改脚本</h3>cd/usr/local/zabbix/share/zabbix/exter nalscripts目录下创建一个命名Kubernetes的目录，把get _k8s.py脚本放到此目录。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/a9ac3acf108346717ca6b1e358b4229b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/a9ac3acf108346717ca6b1e358b4229b.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/8b38649afa34e9f1e03b705c90c52bea.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/8b38649afa34e9f1e03b705c90c52bea.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
需要修改脚本三个地方。<br>
<br>上传外部检查get _k8s脚本到/usr/local/zabbix/share/zabbix/exter nalscript目录。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/747774732f02545ebcaffc4136722e7e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/747774732f02545ebcaffc4136722e7e.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>第四步：创建主机并且套用脚本</h3>注意：主机名称必须是k8s_master，否则无法获取数据。（因为数据是通过Zabbix_sender发送到该主机）<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/739c24f6a96ceb93db0f3b85f16e9d49.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/739c24f6a96ceb93db0f3b85f16e9d49.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/309983ce5d40089f02aece9252d7ee70.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/309983ce5d40089f02aece9252d7ee70.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>第五步：手动触发脚本</h3>选中该监控项，点击立即检查。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/b7972a81c4bea80fc101a85665262b75.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/b7972a81c4bea80fc101a85665262b75.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
数据效果：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210422/bcba73359dee23b7efabf6bb3ac2519e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210422/bcba73359dee23b7efabf6bb3ac2519e.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Zabbix通过API获取Kubernetes结果成功。<br>
<br>原文链接：<a href="https://www.xlsys.cn/1778.html" rel="nofollow" target="_blank">https://www.xlsys.cn/1778.html</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            