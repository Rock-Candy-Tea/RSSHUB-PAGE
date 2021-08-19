
---
title: '如何将Docker 镜像从1.43G瘦身到22.4MB'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/e343ae03161fb94de5dd5ccff887428a.jpeg'
author: Dockone
comments: false
date: 2021-08-19 13:15:41
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/e343ae03161fb94de5dd5ccff887428a.jpeg'
---

<div>   
<br>【编者的话】Docker镜像的大小对于系统的CICD有很大影响，尤其是云部署的机器，我们在生产实践中都会做瘦身的操作，尽最大的可能使用Size小的镜像完成功能。下文是一个简单的ReactJS程序上线的瘦身体验，希望可以帮助大家找到镜像瘦身的方向和灵感。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/e343ae03161fb94de5dd5ccff887428a.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/e343ae03161fb94de5dd5ccff887428a.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>如果你正在做web开发相关工作，那么你可能已经知道容器化的概念，以及知道它强大的功能等等。<br>
<br>但在使用Docker时，镜像大小至关重要。我们从create-react-app获得的样板项目通常都超过1.43 GB。<br>
<br>今天，我们将容器化一个ReactJS应用程序，并学习一些关于如何减少镜像大小并提高性能的技巧。<br>
<br>我们将以ReactJS为例，但它适用于任何类型的NodeJS应用程序。<br>
<br><h2>步骤1. 创建项目</h2><ul><li>借助脚手架通过命令行模式创建React项目</li></ul><br>
<br><pre class="prettyprint">npx create-react-app docker-image-test<br>
</pre><br>
<ul><li>项目创建成功后讲生成一个基础React应用程序架构</li><li>我们可以进入项目目录并运行项目</li></ul><br>
<br><pre class="prettyprint">cd docker-image-test<br>
yarn install<br>
yarn start<br>
</pre><br>
<ul><li>通过访问 <a href="http://localhost:3000/" rel="nofollow" target="_blank">http://localhost:3000</a>可以访问已经启动的应用程序</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/426830d75249ff2a83b0d27cfd5e2c0d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/426830d75249ff2a83b0d27cfd5e2c0d.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>步骤2:构建第一个镜像</h2>在项目的根目录中创建一个名为Dockerfile的文件，并粘贴以下代码：<br>
<br><pre class="prettyprint">FROM node:12<br>
<br>
WORKDIR /app<br>
<br>
COPY package.json ./<br>
<br>
RUN yarn install<br>
<br>
COPY . .<br>
<br>
EXPOSE 3000<br>
<br>
CMD ["yarn", "start"]<br>
</pre><br>
<ul><li>注意，这里我们从docker仓库获得基础镜像 Node:12  然后安装依赖项并运行基本命令。(我们不会在这里讨论docker命令的细节)</li><li>现在从终端为容器构建镜像</li></ul><br>
<br><pre class="prettyprint">docker build -t docker-image-test .<br>
</pre><br>
<ul><li><br>Docker构建镜像完成之后，您可以使用此命令查看您的镜像:<br>
<br><pre class="prettyprint">docker images<br>
</pre><br>
在查询结果列表的顶部，是我们新创建的图像，在最右边，我们可以看到图像的大小。目前是1.43GB。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/ba9391612216eba1e81390dff1e327d1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/ba9391612216eba1e81390dff1e327d1.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>我们使用以下命令运行镜像<br>
<pre class="prettyprint">docker run --rm -it -p 3000:3000/tcp docker-image-test:latest<br>
</pre></li></ul><br>
<br>打开浏览器并且刷新页面验证其可以正常运行。<br>
<br><h2>步骤3：修改基础镜像</h2>- 先前的配置中我们用node:12作为基础镜像。但是传统的node镜像是基于Ubuntu的，对于我们简单的React应用程序来说这大可不必。<br>
<ul><li>从DockerHub(官方docker镜像注册表)中我们可以看到，基于alpine-based 的node镜像比基于ubuntu的镜像小得多，而且它们的依赖程度非常低。</li><li>下面显示了这些基本图像的大小比较</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/fc4e095c9d242aaa40b2dc806e06a4aa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/fc4e095c9d242aaa40b2dc806e06a4aa.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>现在我们将使用node:12-alpine作为我们的基础镜像，看看会发生什么。<br>
<pre class="prettyprint">FROM node:12-alpine<br>
<br>
WORKDIR /app<br>
<br>
COPY package.json ./<br>
<br>
RUN yarn install<br>
<br>
COPY . .<br>
<br>
EXPOSE 3000<br>
<br>
CMD ["yarn", "start"]<br>
</pre><br>
<br>然后我们以此构建我们的镜像，并与之前做对比。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/f84bfe118ef93847403e729ba15253af.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/f84bfe118ef93847403e729ba15253af.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>哇!我们的镜像大小减少到只有580MB，这是一个很大的进步。但还能做得更好吗?<br>
<br><h2>步骤4：多级构建</h2><ul><li>在之前的配置中，我们会将所有源代码也复制到工作目录中。</li><li>但这大可不必，因为从发布和运行来看我们只需要构建好的运行目录即可。因此，现在我们将引入多级构建的概念，以减少不必要的代码和依赖于我们的最终镜像。</li></ul><br>
<br><pre class="prettyprint"><h1>STAGE 1</h1>FROM node:12-alpine AS build<br>
<br>
WORKDIR /app<br>
<br>
COPY package.json ./<br>
<br>
RUN yarn  install<br>
<br>
COPY . /app<br>
<br>
RUN yarn build<br>
<br>
<h1>STAGE 2</h1>FROM node:12-alpine<br>
<br>
WORKDIR /app<br>
<br>
RUN npm install -g webserver.local<br>
<br>
COPY --from=build /app/build ./build<br>
<br>
EXPOSE 3000<br>
<br>
CMD webserver.local -d ./build<br>
</pre><br>
<ul><li>在第一阶段，安装依赖项并构建我们的项目</li><li>在第二阶段，我们复制上一阶段构建产物目录，并使用它来运行应用程序。</li><li>这样我们在最终的镜像中就不会有不必要的依赖和代码。</li></ul><br>
<br>接下来，构建镜像成功后并从列表中查看镜像<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/460acc6fca669af78c8c939e71070757.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/460acc6fca669af78c8c939e71070757.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>现在我们的镜像大小只有97.5MB。这简直太棒了。<br>
<br><h2>步骤5：使用Nginx</h2><ul><li>我们正在使用node服务器运行ReactJS应用程序的静态资源，但这不是静态资源运行的最佳选择。</li><li>我们尝试使用Nginx这类更高效、更轻量级的服务器来运行资源应用程序，也可以尽可能提高其性能，并且减少镜像的量。</li><li>我们最终的Docker配置文件看起来像这样</li></ul><br>
<br><pre class="prettyprint"><h1>STAGE 1</h1>FROM node:12-alpine AS build<br>
<br>
WORKDIR /app<br>
<br>
COPY package.json ./<br>
<br>
RUN yarn  install<br>
<br>
COPY . /app<br>
<br>
RUN yarn build<br>
<h1>STAGE 2</h1>FROM nginx:stable-alpine<br>
<br>
COPY --from=build /app/build /usr/share/nginx/html<br>
<br>
EXPOSE 80<br>
<br>
CMD ["nginx", "-g", "daemon off;"]<br>
</pre><br>
<ul><li>我们正在改变docker配置的第二阶段，以使用Nginx来服务我们的应用程序。</li><li>然后使用当前配置构建镜像。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/f7c132a9d7b188034334546ec05112dd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/f7c132a9d7b188034334546ec05112dd.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>镜像大小减少到只有22.4MB !</li><li>同时，我们正在使用一个性能更好的服务器来服务我们出色的应用程序。</li><li>我们可以使用以下命令验证应用程序是否仍在工作。</li></ul><br>
<br><pre class="prettyprint">docker run --rm  -it -p 3000:80/tcp docker-image-test:latest<br>
</pre><br>
<ul><li>注意，我们将容器的80端口暴露给外部，因为默认情况下，Nginx将在容器内部的80端口上可用。<br>
所以这些是一些简单的技巧，你可以应用到你的任何NodeJS项目，以大幅减少镜像大小。<br>
现在，您的容器确实更加便携和高效了。</li></ul><br>
<br>今天就到这里。编码快乐!<br>
<br><strong>原文链接：<a href="https://javascript.plainenglish.io/how-i-reduced-docker-image-size-from-1-43-gb-to-22-4-mb-84058d70574b">how-i-reduced-docker-image-size-from-1-43-gb-to-22-4-mb</a></strong> trans by ylzhang
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            