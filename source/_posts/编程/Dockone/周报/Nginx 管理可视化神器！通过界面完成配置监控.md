
---
title: 'Nginx 管理可视化神器！通过界面完成配置监控'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210607/2a83138348ab645125d32f9343021942.png'
author: Dockone
comments: false
date: 2021-06-10 04:22:14
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210607/2a83138348ab645125d32f9343021942.png'
---

<div>   
<br><h3>需求</h3>Nginx 可视化管理，例如：<br>
<ul><li>配置管理</li><li>性能监控</li><li>日志监控</li><li>其他配置</li></ul><br>
<br><h3>方案</h3>目前已实现前两条，配置管理和性能监控。<br>
<br>日志分析监控这块还需要另找方案实现！<br>
<br>目前方案直接套用 GitHub 大神开发的 nginx-gui，GitHub 地址：<a href="https://github.com/onlyGuo/nginx-gui" rel="nofollow" target="_blank">https://github.com/onlyGuo/nginx-gui</a><br>
<br>这个东西真的要吹一波，太好用了，而且源码公开，解决了我这种 Java 出身的 Linux 菜鸟的一大难题！<br>
<br>界面截图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210607/2a83138348ab645125d32f9343021942.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210607/2a83138348ab645125d32f9343021942.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210607/1f7356c96447aa8a901a0e6e6f2ca828.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210607/1f7356c96447aa8a901a0e6e6f2ca828.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210607/d035ac7d243e19ccda67b3f2cb80b098.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210607/d035ac7d243e19ccda67b3f2cb80b098.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210607/ac411d62b8d35935eff9b421cb6db53d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210607/ac411d62b8d35935eff9b421cb6db53d.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>说明</h3>先说明下，我也是刚才现学的，只是写下折腾的过程和碰到的问题<br><br>
详细的用法之类的还是建议访问作者的 GitHub 和作者的博客查看。<br>
<br>作者 GitHub：<a href="https://github.com/onlyGuo/nginx-gui" rel="nofollow" target="_blank">https://github.com/onlyGuo/nginx-gui</a><br>
<br>作者博客：<a href="http://bl.321aiyi.com/2019/03/18/nginx-gui/" rel="nofollow" target="_blank">http://bl.321aiyi.com/2019/03/18/nginx-gui/</a><br>
<h3>折腾</h3><h4>下载和配置</h4>首先到作者 GitHub 说明页面，下载对应系统版本的安装包。<br>
<br>需要注意的是 Linux 版本有一段描述不可忽视：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210607/a15015d9409d6dbdef74eadfe76942d1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210607/a15015d9409d6dbdef74eadfe76942d1.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
配置步骤如下：<br>
<br>1、下载并解压 <code class="prettyprint">Nginx-GUI-For-Linux-1.0.zip</code><br>
<br>略<br>
<br>2、修改配置文件<br>
<br>文件位置：<code class="prettyprint">conf/conf.properties</code><br>
<pre class="prettyprint"># Nginx 安装路径<br>
nginx.path = /usr/local/Cellar/nginx/1.15.12<br>
# Nginx 配置文件全路径<br>
nginx.config = /Users/gsk/dev/apps/nginx-1.15.12/conf/nginx.conf<br>
<h1> </h1>account.admin = admin<br>
</pre><br>
3、重命名（此步骤仅Linux版本需要）<br>
<br>根据原作者的描述，针对 Linux 64 位版本，需要将 <code class="prettyprint">lib/bin/</code> 下的 <code class="prettyprint">java_vms</code> 文件重命名为 <code class="prettyprint">java_vms_nginx_gui</code>。<br>
<h4>在服务器上运行</h4>前面的步骤都完成以后，直接打包发布到服务器<br>
<pre class="prettyprint"># 赋权<br>
sudo chmod -R 777 nginx-gui/<br>
<br>
# 后台启动<br>
nohup bash /root/web/nginx-gui/startup.sh > logs/nginx-gui.out &<br>
</pre><br>
访问默认端口 8889 默认账号密码都是 admin。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210607/043ecd5b9355d23623f5815a6ae7a16e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210607/043ecd5b9355d23623f5815a6ae7a16e.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>目前状况</h3>目前最新的版本为 V1.6，已实现不少新功能和修复了已知的所有 bug，推荐大家使用最新版本，分分钟搞定 Nginx。<br>
<br>原文链接：<a href="https://leanote.zzzmh.cn/blog/post/5cc7f63616199b068300001c" rel="nofollow" target="_blank">https://leanote.zzzmh.cn/blog/ ... 0001c</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            