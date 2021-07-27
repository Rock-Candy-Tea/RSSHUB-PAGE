
---
title: 'Docker制作镜像'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2836'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 22:15:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=2836'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.准备文件</h2>
<pre><code class="copyable">touch Dockerfile
docker search centos
docker pull cent
docker images
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2.编写Dockerfile</h2>
<pre><code class="hljs language-dockerfile copyable" lang="dockerfile"><span class="hljs-comment"># 打包依赖阶段使用golang作为基础镜像</span>
<span class="hljs-keyword">FROM</span> golang:<span class="hljs-number">1.16</span> as builder

<span class="hljs-comment"># 启用go module</span>
<span class="hljs-keyword">ENV</span> GO111MODULE=on \
    GOPROXY=https://goproxy.cn,direct

<span class="hljs-keyword">WORKDIR</span><span class="bash"> /app</span>

<span class="hljs-keyword">COPY</span><span class="bash"> . .</span>

<span class="hljs-comment"># 指定OS等，并go build</span>
<span class="hljs-keyword">RUN</span><span class="bash"> GOOS=linux GOARCH=amd64 go build .</span>

<span class="hljs-comment"># 由于我不止依赖二进制文件，还依赖views文件夹下的html文件还有assets文件夹下的一些静态文件</span>
<span class="hljs-comment"># 所以我将这些文件放到了publish文件夹</span>
<span class="hljs-comment">#RUN mkdir publish && cp toc-generator publish && \</span>
<span class="hljs-comment">#    cp -r views publish && cp -r assets publish</span>

<span class="hljs-comment"># 运行阶段指定scratch作为基础镜像</span>
<span class="hljs-keyword">FROM</span> alpine

<span class="hljs-keyword">LABEL</span><span class="bash"> maintainer=<span class="hljs-string">"xuehu96@vip.qq.com"</span></span>
<span class="hljs-keyword">LABEL</span><span class="bash"> version=<span class="hljs-string">"1.0"</span></span>
<span class="hljs-keyword">LABEL</span><span class="bash"> description=<span class="hljs-string">"TTTT  EEEE SSS T"</span></span>

<span class="hljs-keyword">WORKDIR</span><span class="bash"> /app</span>

<span class="hljs-comment"># 将上一个阶段publish文件夹下的所有文件复制进来</span>
<span class="hljs-keyword">COPY</span><span class="bash"> --from=builder /app .</span>

<span class="hljs-comment"># 指定运行时环境变量</span>
<span class="hljs-comment">#ENV GIN_MODE=release \</span>
<span class="hljs-comment">#    PORT=80</span>

<span class="hljs-keyword">EXPOSE</span> <span class="hljs-number">12345</span>

<span class="hljs-keyword">ENTRYPOINT</span><span class="bash"> [<span class="hljs-string">"./main"</span>]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3.制作容器</h2>
<pre><code class="hljs language-bash copyable" lang="bash">sudo docker build -t dockgo . 

<span class="hljs-comment">#测试</span>
docker run -d p:12345:12345 dockgo
sudo docker run -d -p 12345:12345 dockgo
sudo docker run -it -p 12345:12345 dockgo
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4.将制作好的镜像打成 tar 包</h2>
<p>　格式：<code>sudo docker save -o dockergo.tar dockgo</code></p>
<h2 data-id="heading-4">5.使用 tar 包</h2>
<p>sudo docker image rm 9e37e0dbdd5c</p>
<p>sudo docker load < tar 包所在路径</p>
<h2 data-id="heading-5">6.删除已经退出的container</h2>
<pre><code class="hljs language-bash copyable" lang="bash">docker rm $(docker ps -aq) 
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            