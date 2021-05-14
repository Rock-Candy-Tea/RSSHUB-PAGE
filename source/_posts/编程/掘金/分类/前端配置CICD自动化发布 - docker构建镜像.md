
---
title: '前端配置CICD自动化发布 - docker构建镜像'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9de4ddb13e447f09de37990ba392086~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 23:02:18 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9de4ddb13e447f09de37990ba392086~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>保持线上项目稳定运行是很重要的，为了达到服务可用性在99.9%，也为了减少开发人员在项目部署时耗费大量精力，可以尝试自动化发布</p>
<p>自动化部署涉及到的配置比较多，每个环节需要掌握的知识也不同，所以分开写</p>
<p>该过程中用到的技术栈<code>webpack</code> <code>docker</code> <code>nginx</code> <code>shell</code></p>
<h2 data-id="heading-1">二、实践环境</h2>
<ul>
<li>mac</li>
<li>node > 10.11.1</li>
<li>docker > 20.0.0</li>
</ul>
<h2 data-id="heading-2">三、提前准备的内容</h2>
<ul>
<li>通过<code>create-react-app</code>构建的一个前端项，这里起名项目<code>myweb</code></li>
<li>本地安装docker</li>
</ul>
<h2 data-id="heading-3">四、构建docker镜像</h2>
<p>首先通过镜像打包前端部署包，在项目根目录下，新建Dockerfile文件</p>
<h3 data-id="heading-4">1、Dockerfile</h3>
<pre><code class="copyable">FROM node:10-alpine as builder

WORKDIR /data/myweb

COPY . .

RUN npm install --registry=https://registry.npm.taobao.org --no-package-lock --no-save

RUN yarn build



FROM nginx:alpine as myweb

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone 

WORKDIR /data/myweb

COPY ./nginx /etc/nginx/conf.d

COPY  --from=builder /data/myweb/build /data/myweb

EXPOSE 80,443
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2、配置文件说明：</h3>
<p>该Dockerfile干了两件事，</p>
<p>第一是将前端项目打包到node镜像中，这里起名builder</p>
<p>第二是拉取nginx镜像，将文件的nginx配置镜像覆盖，将builder镜像中打包的文件复制到nginx镜像的<code>/data/myweb</code>文件中，执行<code>docker build -t myweb .</code></p>
<p>此时我们执行打包命令,得到的两个镜像，一个打包后的node镜像，一个nginx镜像，我们只需要nginx镜像来拉起服务</p>
<h3 data-id="heading-6">3、执行命令</h3>
<pre><code class="copyable">// 1、docker通过Dockerfile构建镜像
`docker build -t dockerName:1.0.0 .`

// 2、查看当前存在镜像
docker images

// 3、删除docker镜像
docker rmi dockerImageId

// 4、删除docker容器
docker rm dockerContainerId

// 5、启动一个docker容器
docker run -d -p 8000:80 --name frontend [dockerImageName]

// 6、查看运行中的容器
docker ps
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4、运行中的服务</h3>
<p>我们可以看到当前运行中的容器</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9de4ddb13e447f09de37990ba392086~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在浏览器访问<code>http://localhost:8000</code>即可看到当前通过docker部署的服务</p>
<h2 data-id="heading-8">五、nginx配置文件</h2>
<p>和我们正常部署是一样的，用来转发静态资源
在根目录下新建nginx文件夹，<code>/nginx/default.conf</code></p>
<pre><code class="copyable">server &#123;
    listen 80;
    server_name localhost;

    location / &#123;
        root /data/myweb;
        index index.html;
    &#125;

    error_page 500 502 503 504 /50x.html;
    location = /50x.html &#123;
        root /usr/share/nginx/html;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们完成了第一步，通过docker部署我们的服务。</p>
<p>如果我们直接通过docker部署前端也是可以的。</p>
<p>接着，有了docker部署的基础，</p>
<p>接着继续通过k8s集群的部署</p></div>  
</div>
            