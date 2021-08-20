
---
title: '如何将Docker镜像从1.43G瘦身到22.4MB'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/e343ae03161fb94de5dd5ccff887428a.jpeg'
author: Dockone
comments: false
date: 2021-08-20 04:09:13
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/e343ae03161fb94de5dd5ccff887428a.jpeg'
---

<div>   
<br>【编者的话】Docker镜像的大小对于系统的CI/CD有很大影响，尤其是云部署的机器，我们在生产实践中都会做瘦身的操作，尽最大的可能使用Size小的镜像完成功能。下文是一个简单的ReactJS程序上线的瘦身体验，希望可以帮助大家找到镜像瘦身的方向和灵感。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/e343ae03161fb94de5dd5ccff887428a.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/e343ae03161fb94de5dd5ccff887428a.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
如果你正在做Web开发相关工作，那么你可能已经知道容器化的概念，以及知道它强大的功能等等。<br>
<br>但在使用Docker时，镜像大小至关重要。我们从<a href="https://reactjs.org/docs/create-a-new-react-app.html">create-react-app</a>获得的样板项目通常都超过1.43 GB。<br>
<br>今天，我们将容器化一个ReactJS应用程序，并学习一些关于如何减少镜像大小并提高性能的技巧。<br>
<br>我们将以ReactJS为例，但它适用于任何类型的NodeJS应用程序。<br>
<h3>步骤1. 创建项目</h3>1、借助脚手架通过命令行模式创建React项目<br>
<pre class="prettyprint">npx create-react-app docker-image-test<br>
</pre><br>
2、项目创建成功后讲生成一个基础React应用程序架构<br>
<br>3、我们可以进入项目目录并运行项目<br>
<pre class="prettyprint">cd docker-image-test<br>
yarn install<br>
yarn start<br>
</pre><br>
4、通过访问<a href="http://localhost:3000/" rel="nofollow" target="_blank">http://localhost:3000</a>可以访问已经启动的应用程序<br>
 <div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/426830d75249ff2a83b0d27cfd5e2c0d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/426830d75249ff2a83b0d27cfd5e2c0d.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>步骤2：构建第一个镜像</h3>1、在项目的根目录中创建一个名为Dockerfile的文件，并粘贴以下代码：<br>
<pre class="prettyprint">FROM node:12<br>
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
2、注意，这里我们从Docker仓库获得基础镜像Node:12，然后安装依赖项并运行基本命令。（我们不会在这里讨论Docker命令的细节）<br>
<br>3、现在从终端为容器构建镜像<br>
<pre class="prettyprint">docker build -t docker-image-test .<br>
</pre><br>
4、Docker构建镜像完成之后，你可以使用此命令查看你的镜像：<br>
<pre class="prettyprint">docker images<br>
</pre><br>
在查询结果列表的顶部，是我们新创建的图像，在最右边，我们可以看到图像的大小。目前是1.43GB。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/ba9391612216eba1e81390dff1e327d1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/ba9391612216eba1e81390dff1e327d1.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
5、我们使用以下命令运行镜像<br>
<pre class="prettyprint">docker run --rm -it -p 3000:3000/tcp docker-image-test:latest<br>
</pre><br>
打开浏览器并且刷新页面验证其可以正常运行。<br>
<h3>步骤3：修改基础镜像</h3>1、先前的配置中我们用node:12作为基础镜像。但是传统的Node镜像是基于Ubuntu的，对于我们简单的React应用程序来说这大可不必。<br>
<br>2、从DockerHub（官方Docker镜像注册表）中我们可以看到，基于alpine-based的Node镜像比基于Ubuntu的镜像小得多，而且它们的依赖程度非常低。<br>
<br>3、下面显示了这些基本图像的大小比较<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/fc4e095c9d242aaa40b2dc806e06a4aa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/fc4e095c9d242aaa40b2dc806e06a4aa.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
现在我们将使用node:12-alpine作为我们的基础镜像，看看会发生什么。<br>
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
然后我们以此构建我们的镜像，并与之前做对比。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/f84bfe118ef93847403e729ba15253af.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/f84bfe118ef93847403e729ba15253af.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
哇！我们的镜像大小减少到只有580MB，这是一个很大的进步。但还能做得更好吗？<br>
<h3>步骤4：多级构建</h3>1、在之前的配置中，我们会将所有源代码也复制到工作目录中。<br>
<br>2、但这大可不必，因为从发布和运行来看我们只需要构建好的运行目录即可。因此，现在我们将引入多级构建的概念，以减少不必要的代码和依赖于我们的最终镜像。<br>
<br>3、配置是这样的：<br>
<pre class="prettyprint"># STAGE 1<br>
<br>
FROM node:12-alpine AS build<br>
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
<br>
# STAGE 2<br>
<br>
FROM node:12-alpine<br>
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
4、在第一阶段，安装依赖项并构建我们的项目<br>
<br>5、在第二阶段，我们复制上一阶段构建产物目录，并使用它来运行应用程序。<br>
<br>6、这样我们在最终的镜像中就不会有不必要的依赖和代码。<br>
<br>接下来，构建镜像成功后并从列表中查看镜像<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/460acc6fca669af78c8c939e71070757.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/460acc6fca669af78c8c939e71070757.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
现在我们的镜像大小只有97.5MB。这简直太棒了。<br>
<h3>步骤5：使用Nginx</h3>1、我们正在使用Node服务器运行ReactJS应用程序的静态资源，但这不是静态资源运行的最佳选择。<br>
<br>2、我们尝试使用Nginx这类更高效、更轻量级的服务器来运行资源应用程序，也可以尽可能提高其性能，并且减少镜像的量。<br>
<br>3、我们最终的Docker配置文件看起来像这样<br>
<pre class="prettyprint"># STAGE 1<br>
<br>
FROM node:12-alpine AS build<br>
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
# STAGE 2<br>
<br>
FROM nginx:stable-alpine<br>
<br>
COPY --from=build /app/build /usr/share/nginx/html<br>
<br>
EXPOSE 80<br>
<br>
CMD ["nginx", "-g", "daemon off;"] <br>
</pre><br>
<br>4、我们正在改变Docker配置的第二阶段，以使用Nginx来服务我们的应用程序。<br>
<br>5、然后使用当前配置构建镜像。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210819/f7c132a9d7b188034334546ec05112dd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210819/f7c132a9d7b188034334546ec05112dd.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
6、镜像大小减少到只有22.4MB！<br>
<br>7、同时，我们正在使用一个性能更好的服务器来服务我们出色的应用程序。<br>
<br>8、我们可以使用以下命令验证应用程序是否仍在工作。<br>
<pre class="prettyprint">docker run --rm  -it -p 3000:80/tcp docker-image-test:latest<br>
</pre><br>
9、注意，我们将容器的80端口暴露给外部，因为默认情况下，Nginx将在容器内部的80端口上可用。<br>
<br>所以这些是一些简单的技巧，你可以应用到你的任何NodeJS项目，以大幅减少镜像大小。<br>
<br>现在，您的容器确实更加便携和高效了。<br>
<br>今天就到这里。编码快乐！<br>
<br><strong>原文链接：<a href="https://javascript.plainenglish.io/how-i-reduced-docker-image-size-from-1-43-gb-to-22-4-mb-84058d70574b">How I Reduced Docker Image Size from 1.43 GB to 22.4 MB</a>（翻译：ylzhang）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            