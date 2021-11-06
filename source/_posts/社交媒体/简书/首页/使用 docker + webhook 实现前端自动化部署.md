
---
title: '使用 docker + webhook 实现前端自动化部署'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://www.jianshu.com/p/undefined'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://www.jianshu.com/p/undefined'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1200" data-height="557"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-4fa208f8d236f3e9" data-original-width="1200" data-original-height="557" data-original-format="image/png" data-original-filesize="26483" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<h1>前言</h1>
<p>得益于 node 的横空出世以及前端工程化的兴起，无论是开发模式，还是开发框架，前端生态链都产生了翻天覆地的变化，与此同时前端慢慢开始向其他领域探索，项目部署就是其中一个领域</p>
<p>在刀耕火种的时代，当执行 <code>npm run build</code> 将生成产物交给运维后，前端的任务就算完成了，运维同学在生产服务器上将产物的路径写入 nginx 配置文件，至此完成了“简单”的部署</p>
<p>随着项目的不断迭代，前端开始发现问题的严重性，每次都需要耗费大量的时间在打包上，<code>开发5分钟，打包半小时的情况屡见不鲜</code>，另外开发者自身环境的差异会导致最终的产物也有不同</p>
<p>但办法总比困难多，例如可以将打包操作放到远端服务器上，又比如可以将上述流程结合 git 仓库实现自动部署</p>
<p>本着不设边界的“字节范”，本文将从零开始，实现前端自动化部署流程，打开项目部署的“黑盒”</p>
<p>涉及技术栈如下：</p>
<ul>
<li><p>docker</p></li>
<li><p>node</p></li>
<li><p>pm2</p></li>
<li><p>shell</p></li>
<li><p>webhook</p></li>
</ul>
<p><code>文章中的命令大部分为 linux 命令，本地是 windows 系统的读者请使用 git bash</code></p>
<h1>介绍 docker</h1>
<p>着手开发前，先介绍这次的主角 <code>docker</code></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="400" data-height="331"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-c5db27195d6ae7ff" data-original-width="400" data-original-height="331" data-original-format="image/png" data-original-filesize="17750" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<h2>什么是 docker</h2>
<p>简而言之，docker 可以灵活的创建/销毁/管理多个“服务器”，这些“服务器”被称为 <code>容器 (container)</code></p>
<p>在容器中你可以做任何服务器可以做的事，例如在有 node 环境的容器中运行 <code>npm run build</code> 打包项目，在有 nginx 环境的容器中部署项目，在有 mysql 环境的容器中做数据存储等等</p>
<p>一旦服务器安装了 docker ，就可以自由创建任意多的容器，上图中 docker 的 logo 形象的展示了它们之间的关系，🐳就是 docker，上面的一个个集装箱就是容器</p>
<h2>安装 docker</h2>
<p>为了方便本地调试，可以先在本地安装 docker</p>
<p>Mac：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdownload.docker.com%2Fmac%2Fstable%2FDocker.dmg" target="_blank">https://download.docker.com/mac/stable/Docker.dmg</a></p>
<p>Windows：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdownload.docker.com%2Fwin%2Fstable%2FDocker%2520for%2520Windows%2520Installer.exe" target="_blank">https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe</a></p>
<p>Linux：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fget.docker.com%2F" target="_blank">https://get.docker.com/</a></p>
<p>下载安装完毕后，点击 docker 图标启动 docker，此时在终端中就可以使用 docker 相关的操作</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2636" data-height="904"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-8c6f824d138cf435" data-original-width="2636" data-original-height="904" data-original-format="image/png" data-original-filesize="183061" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>出现以下情况，检查 docker 应用程序是否正常启动</p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n36" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="html" cid="n58" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;"><br>
<h1>Hello docker</h1></pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="dockerfile" cid="n59" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;"># Dockerfile<br>
FROM nginx<br>
COPY index.html /usr/share/nginx/html/index.html<br>
EXPOSE 80</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="" cid="n69" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">hello-docker<br>
|____index.html<br>
|____Dockerfile</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n72" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">docker build . -t test-image:latest </pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n85" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">docker run -d -p 80:80  --name test-container test-image:latest</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n102" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">docker pull nginx<br>
docker run -d -p 81:80  --name nginx-container nginx</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n155" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">less ~/.ssh/id_rsa.pub </pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n158" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">$ ssh-keygen -o<br>
Generating public/private rsa key pair.<br>
Enter file in which to save the key (/home/schacon/.ssh/id_rsa):<br>
Created directory '/home/schacon/.ssh'.<br>
Enter passphrase (empty for no passphrase):<br>
Enter same passphrase again:<br>
Your identification has been saved in /home/schacon/.ssh/id_rsa.<br>
Your public key has been saved in /home/schacon/.ssh/id_rsa.pub.<br>
The key fingerprint is:<br>
d0:82:24:8e:d7:f1:bb:9b:33:53:96:93:49:da:9b:e3 schacon@mylaptop.local</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n159" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">$ cat ~/.ssh/id_rsa.pub<br>
ssh-rsa AAAAB3NzaCxxxxxxxxxxxxxxxxxxxxxxxxBWDSU<br>
GPl+nafzlHDTYxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxPppSwg0cda3<br>
Pbv7kOdJ/MxxxxxxxxxxxxxxxxxxxxxxxxxxxQwdsdMFvSlVK/7XA<br>
t3FaoJoxxxxxxxxxxxxxxxxxxxxx88XypNDvjYNby6vw/Pb0rwert/En<br>
mZ+AW4OZPnTxxxxxxxxxxxxxxxxxxo1d01QraTlMqVSsbx<br>
NrRFi9wrf+M7Q== schacon@mylaptop.local</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n164" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">ssh <username>@<hostname or IP address></pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n170" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;"># Step 1: 安装必要的一些系统工具<br>
sudo yum install -y yum-utils</p>
<h1>Step 2: 添加软件源信息，使用阿里云镜像</h1>
<p>sudo yum-config-manager --add-repo <a href="https://links.jianshu.com/go?to=http%3A%2F%2Fmirrors.aliyun.com%2Fdocker-ce%2Flinux%2Fcentos%2Fdocker-ce.repo" target="_blank">http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo</a></p>
<h1>Step 3: 安装 docker-ce</h1>
<p>sudo yum install docker-ce docker-ce-cli containerd.io</p>
<h1>Step 4: 开启 docker服务</h1>
<p>sudo systemctl docker start</p>
<h1>Step 5: 运行 hello-world 项目</h1>
<p>sudo docker run hello-world</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n174" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">yum install git</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n179" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">curl -o- <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fraw.githubusercontent.com%2Fnvm-sh%2Fnvm%2Fv0.34.0%2Finstall.sh" target="_blank">https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh</a> | bash</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n181" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">export NVM_DIR="<img class="math-inline" src="https://math.jianshu.com/math?formula=HOME%2F.nvm%22%20%5B%20-s%20%22" alt="HOME/.nvm" [ -s "" mathimg="1" referrerpolicy="no-referrer">NVM_DIR/nvm.sh" ] && . "<img class="math-inline" src="https://math.jianshu.com/math?formula=NVM_DIR%2Fnvm.sh%22%20%23%20This%20loads%20nvm%20%5B%20-s%20%22" alt="NVM_DIR/nvm.sh" # This loads nvm [ -s "" mathimg="1" referrerpolicy="no-referrer">NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion"  # This loads nvm bash_completion</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n183" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">nvm install node</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n186" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">npm i pm2 -g</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n190" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">vue create docker-test</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="dockerfile" cid="n213" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;"># dockerfile</p>
<h1>build stage</h1>
<p>FROM node:latest as build-stage<br>
WORKDIR /app<br>
COPY package*.json ./<br>
RUN npm install<br>
COPY . .<br>
RUN npm run build<br>
​</p>
<h1>production stage</h1>
<p>FROM nginx:latest as production-stage<br>
COPY --from=build-stage /app/dist /usr/share/nginx/html<br>
EXPOSE 80<br>
CMD ["nginx", "-g", "daemon off;"]</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n240" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">scp ./Dockerfile root@118.89.244.45:/root</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n244" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;"># .dockerignore<br>
node_modules</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n249" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">scp ./.dockerignore root@118.89.244.45:/root</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="javascript" cid="n253" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">const http = require("http")<br>
​<br>
http.createServer((req, res) => &#123;<br>
console.log('receive request')<br>
console.log(req.url)<br>
if (req.method === 'POST' && req.url === '/') &#123;<br>
//...<br>
&#125;<br>
res.end('ok')<br>
&#125;).listen(3000,()=>&#123;<br>
console.log('server is ready')<br>
&#125;)</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="diff" cid="n256" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">const http = require("http")</p>
<ul>
<li>const &#123;execSync&#125; = require("child_process")</li>
<li>const path = require("path")</li>
<li>const fs = require("fs")<br>
​</li>
<li>// 递归删除目录</li>
<li>function deleteFolderRecursive(path) &#123;</li>
<li>if( fs.existsSync(path) ) &#123;</li>
<li><pre><code>   fs.readdirSync(path).forEach(function(file) &#123;
</code></pre></li>
<li><pre><code>       const curPath = path + "/" + file;
</code></pre></li>
<li><pre><code>       if(fs.statSync(curPath).isDirectory()) &#123; // recurse
</code></pre></li>
<li><pre><code>           deleteFolderRecursive(curPath);
</code></pre></li>
<li><pre><code>       &#125; else &#123; // delete file
</code></pre></li>
<li><pre><code>           fs.unlinkSync(curPath);
</code></pre></li>
<li><pre><code>       &#125;
</code></pre></li>
<li><pre><code>   &#125;);
</code></pre></li>
<li><pre><code>   fs.rmdirSync(path);
</code></pre></li>
<li>&#125;</li>
<li>&#125;<br>
​</li>
<li>const resolvePost = req =></li>
<li>new Promise(resolve => &#123;</li>
<li><pre><code>let chunk = "";
</code></pre></li>
<li><pre><code>   req.on("data", data => &#123;
</code></pre></li>
<li><pre><code>       chunk += data;
</code></pre></li>
<li><pre><code>   &#125;);
</code></pre></li>
<li><pre><code>   req.on("end", () => &#123;
</code></pre></li>
<li><pre><code>    resolve(JSON.parse(chunk));
</code></pre></li>
<li><pre><code>&#125;);
</code></pre></li>
<li>&#125;);<br>
​<br>
http.createServer(async (req, res) => &#123;<br>
console.log('receive request')<br>
console.log(req.url)<br>
if (req.method === 'POST' && req.url === '/') &#123;</li>
<li><pre><code>const data = await resolvePost(req);
</code></pre></li>
<li><pre><code>const projectDir = path.resolve(`./$&#123;data.repository.name&#125;`)
</code></pre></li>
<li><pre><code>deleteFolderRecursive(projectDir)
</code></pre></li>
</ul>
<p>​</p>
<ul>
<li>// 拉取仓库最新代码</li>
<li>execSync(<code>git clone https://github.com/yeyan1996/$&#123;data.repository.name&#125;.git $&#123;projectDir&#125;</code>,&#123;</li>
<li><pre><code>  stdio:'inherit',
</code></pre></li>
<li>&#125;)<br>
&#125;<br>
res.end('ok')<br>
&#125;).listen(3000, () => &#123;<br>
console.log('server is ready')<br>
&#125;)</pre></li>
</ul>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="diff" cid="n270" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">const http = require("http")<br>
const &#123;execSync&#125; = require("child_process")<br>
const fs = require("fs")<br>
const path = require("path")<br>
​<br>
// 递归删除目录<br>
function deleteFolderRecursive(path) &#123;<br>
if( fs.existsSync(path) ) &#123;<br>
fs.readdirSync(path).forEach(function(file) &#123;<br>
const curPath = path + "/" + file;<br>
if(fs.statSync(curPath).isDirectory()) &#123; // recurse<br>
deleteFolderRecursive(curPath);<br>
&#125; else &#123; // delete file<br>
fs.unlinkSync(curPath);<br>
&#125;<br>
&#125;);<br>
fs.rmdirSync(path);<br>
&#125;<br>
&#125;<br>
​<br>
const resolvePost = req =><br>
new Promise(resolve => &#123;<br>
let chunk = "";<br>
req.on("data", data => &#123;<br>
chunk += data;<br>
&#125;);<br>
req.on("end", () => &#123;<br>
resolve(JSON.parse(chunk));<br>
&#125;);<br>
&#125;);<br>
​<br>
http.createServer(async (req, res) => &#123;<br>
console.log('receive request')<br>
console.log(req.url)<br>
if (req.method === 'POST' && req.url === '/') &#123;<br>
const data = await resolvePost(req);<br>
const projectDir = path.resolve(<code>./$&#123;data.repository.name&#125;</code>)<br>
deleteFolderRecursive(projectDir)</p>
<p>// 拉取仓库最新代码<br>
execSync(<code>git clone https://github.com/yeyan1996/$&#123;data.repository.name&#125;.git $&#123;projectDir&#125;</code>,&#123;<br>
stdio:'inherit',<br>
&#125;)</p>
<ul>
<li><pre><code>// 复制 Dockerfile 到项目目录
</code></pre></li>
<li><pre><code>fs.copyFileSync(path.resolve(`./Dockerfile`), path.resolve(projectDir,'./Dockerfile'))
</code></pre></li>
</ul>
<p>​</p>
<ul>
<li><pre><code>// 复制 .dockerignore 到项目目录
</code></pre></li>
<li><pre><code>fs.copyFileSync(path.resolve(__dirname,`./.dockerignore`), path.resolve(projectDir, './.dockerignore'))
</code></pre></li>
</ul>
<p>​</p>
<ul>
<li><pre><code> // 创建 docker 镜像
</code></pre></li>
<li><pre><code>execSync(`docker build . -t $&#123;data.repository.name&#125;-image:latest `,&#123;
</code></pre></li>
<li><pre><code>  stdio:'inherit',
</code></pre></li>
<li><pre><code>  cwd: projectDir
</code></pre></li>
<li>&#125;)<br>
​</li>
<li><pre><code> // 销毁 docker 容器
</code></pre></li>
<li><pre><code> execSync(`docker ps -a -f "name=^$&#123;data.repository.name&#125;-container" --format="&#123;&#123;.Names&#125;&#125;" | xargs -r docker stop | xargs -r docker rm`, &#123;
</code></pre></li>
<li><pre><code>  stdio: 'inherit',
</code></pre></li>
<li>&#125;)<br>
​</li>
<li><pre><code> // 创建 docker 容器
</code></pre></li>
<li><pre><code> execSync(`docker run -d -p 8888:80 --name $&#123;data.repository.name&#125;-container  $&#123;data.repository.name&#125;-image:latest`, &#123;
</code></pre></li>
<li><pre><code>  stdio:'inherit',
</code></pre></li>
<li><pre><code> console.log('deploy success')
</code></pre></li>
<li>&#125;)<br>
res.end('ok')<br>
&#125;<br>
&#125;).listen(3000, () => &#123;<br>
console.log('server is ready')<br>
&#125;)</pre></li>
</ul>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n272" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">scp ./index.js root@118.89.244.45:/root</pre></p>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="shell" cid="n275" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;">pm2 start index.js</pre></p>
<ul>
<li><p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Ftravis-ci.org%2F" target="_blank">travis-ci</a></p></li>
<li>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fcircleci.com%2F" target="_blank">circleci</a></p>
<p>通过 yml 配置文件，简化上文中注册 webhook 和编写更新容器的 index.js 脚本的步骤</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="750" data-height="200"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-61d17d1cf0833826" data-original-width="750" data-original-height="200" data-original-format="image/jpeg" data-original-filesize="17473" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="400" data-height="400"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-f914b3dfd997fe94" data-original-width="400" data-original-height="400" data-original-format="image/png" data-original-filesize="3119" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p><pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="yml" cid="n305" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); --select-text-bg-color:  #36284e; --select-text-font-color:  #fff; font-size: 0.9rem; line-height: 1.714285em; display: block; break-inside: avoid; text-align: left; white-space: normal; background-image: inherit; background-size: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(218, 218, 218); position: relative !important; margin-bottom: 3em; margin-left: 2em; padding-left: 1ch; padding-right: 1ch; width: inherit; background-position: inherit inherit; background-repeat: inherit inherit;"># .travis.yml<br>
language: node_js<br>
node_js:</p>
<ul>
<li>8<br>
branchs:<br>
only:</li>
<li>master<br>
cache:<br>
directories:</li>
<li>node_modules<br>
install:</li>
<li>yarn install<br>
scripts:</li>
<li>yarn test</li>
<li>yarn build</pre></li>
</ul>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.docker.com%2Fdevelop%2Fdevelop-images%2Fdockerfile_best-practices%2F" target="_blank">Best practices for writing Dockerfiles</a></p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fcookbook%2Fdockerize-vuejs-app.html%23Alternative-Patterns" target="_blank">Dockerize Vue.js App</a></p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fshanyue.tech%2F" target="_blank">山月的琐碎博客记录</a></p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fjuejin.im%2Fpost%2F5d8440ebe51d4561eb0b2751" target="_blank">写给前端的Docker实战教程</a></p>
<h1>参考资料</h1>
<p>感谢你能看到这里，希望对各位有帮助～</p>
<p>但本文的宗旨还是探索其中的原理，维护成熟的开源项目还是推荐使用上述平台</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1851" data-height="889"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-63614a4a2176cf64" data-original-width="1851" data-original-height="889" data-original-format="image/jpeg" data-original-filesize="63913" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>另外随着环境的增多，容器也会逐渐增加，docker 也推出了更好管理容器的方式 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.docker.com%2Fcompose%2F" target="_blank">docker-compose</a></p>
</li>
</ul>
<p>基于 github 平台也有非常成熟的 CI/CD 工具，例如</p>
<h1>写在后面</h1>
<p>关注 Dockerfile ，.dockerignore， index.js 文件</p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fyeyan1996%2Fdocker-test" target="_blank">Docker-test</a></p>
<h1>源码</h1>
<p>大功告成～</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2164" data-height="1148"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-3b2029143be2967e" data-original-width="2164" data-original-height="1148" data-original-format="image/png" data-original-filesize="161323" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>最后访问 8888 端口可以看到更新后的文案</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1186" data-height="318"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-83f5053a999afb98" data-original-width="1186" data-original-height="318" data-original-format="image/png" data-original-filesize="460645" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>接着销毁旧容器，并使用更新后的镜像创建容器</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1008" data-height="776"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-db5ea7cafcce8e4e" data-original-width="1008" data-original-height="776" data-original-format="image/png" data-original-filesize="935094" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>克隆完毕后将 Dockerfile 和 .dockerignore 放入项目文件中，并更新镜像</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="846" data-height="180"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-99b906dd761565cf" data-original-width="846" data-original-height="180" data-original-format="image/png" data-original-filesize="151609" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>不出意外，pm2 会输出克隆项目的日志</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1194" data-height="366"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-8b2477b25e415251" data-original-width="1194" data-original-height="366" data-original-format="image/png" data-original-filesize="70067" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>首先在云服务器上运行 <code>pm2 logs</code> 查看 index.js 输出的日志，随后本地添加 <code>hello docker</code> 文案，并推送至 github</p>
<p>来试试自动化部署的流程是否能正常运行</p>
<h1>try it</h1>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2992" data-height="1760"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-71ad3785de76c4fe" data-original-width="2992" data-original-height="1760" data-original-format="image/png" data-original-filesize="257274" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>启动成功后，访问云服务器 8888 端口看到部署的 demo 项目</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1310" data-height="420"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-29e4c808dcc0636d" data-original-width="1310" data-original-height="420" data-original-format="image/png" data-original-filesize="63053" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>通过之前安装的 pm2 将 index.js 作为后台脚本在云服务器上运行</p>
<h2>运行 node 脚本</h2>
<p>同样通过 scp 复制到云服务器上</p>
<p>然后给 index.js 添加 docker 相关逻辑</p>
<p>删除 name 为 docker-container 的容器（停止状态的容器才能被删除）</p>
<blockquote>
<p>docker rm docker-container</p>
</blockquote>
<p>停止 name 为 docker-container 的容器</p>
<blockquote>
<p>docker stop docker-container</p>
</blockquote>
<p>查看所有 name 以 docker 开头的 docker 容器，并只输出容器名</p>
<blockquote>
<p>docker ps -a -f "name=^docker" --format="&#123;&#123;.Names&#125;&#125;"</p>
</blockquote>
<p>在创建新容器前，需要先把旧容器销毁，这里先介绍几个用到的 docker 命令：</p>
<h2>创建镜像和容器</h2>
<p><code>data.repository.name</code> 即 webhook 中记录仓库名的属性</p>
<p>当项目更新后，云服务器需要先拉取仓库最新代码</p>
<h2>拉取仓库代码</h2>
<p>本地项目里新建 index.js</p>
<p>由于我们是前端开发，这里使用 node 开启一个简单的 http 服务器处理 webhook 发送的 post 请求</p>
<h2>创建 http 服务器</h2>
<p>接着将 .dockerignore 文件也复制到云服务器上</p>
<p>第二次复制<strong>除 node_modules</strong>的所有文件</p>
<p>第一次只复制 package.json 和 package-lock.json，并安装依赖</p>
<p>由于需要保持本地和容器中 node_module 依赖包一致，在创建 Dockerfile 时用了两次 <code>COPY</code> 命令</p>
<p>本地项目里新建 .dockerignore</p>
<p>类似 .gitignore，.dockerignore 可以在创建镜像复制文件时忽略复制某些文件</p>
<h2>创建 .dockerignore</h2>
<p>最后通过 <code>scp</code> 命令，将 Dockerfile 文件复制到云服务器上</p>
<ul>
<li><p>FROM nginx:latest as production-stage：基于 nginx 最新镜像，并将有 nginx 环境的阶段命名为 <code>production-stage</code></p></li>
<li><p>COPY --from=build-stage /app/dist /usr/share/nginx/html：通过 --form 参数可以引用 <code>build-stage</code> 阶段生成的产物，将其复制到 /usr/share/nginx/html</p></li>
<li><p>EXPOSE 80：容器对外暴露 80 端口</p></li>
<li><p>CMD ["nginx", "-g", "daemon off;"]：容器创建时运行 <code>nginx -g daemon off</code> 命令，<code>一旦 CMD 对应的命令结束，容器就会被销毁</code>，所以通过 daemon off 让 nginx 一直在前台运行</p></li>
</ul>
<p>将构建分为两个阶段，第一阶段基于 node 镜像，第二阶段基于 nginx 镜像</p>
<p>这里用到了 docker 一个技巧：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.docker.com%2Fdevelop%2Fdevelop-images%2Fmultistage-build%2F" target="_blank">多阶段构建</a></p>
<ul>
<li><p>FROM node:latest as build-stage：基于 node 最新镜像，并通过构建阶段命名，将有 node 环境的阶段命名为 <code>build-stage</code></p></li>
<li><p>WORKDIR /app：将工作区设为 /app，和其他系统文件隔离</p></li>
<li><p>COPY package*.json ./：拷贝 package.json/package-lock.json 到容器的 /app 目录</p></li>
<li><p>RUN npm install：运行 <code>npm install</code> 在容器中安装依赖</p></li>
<li><p>COPY . .：拷贝其他文件到容器 /app 目录，分两次拷贝是因为保持 node_modules 一致</p></li>
<li><p>RUN npm run build：运行 <code>npm run build</code> 在容器中构建</p></li>
</ul>
<p>逐行解析配置：</p>
<p>先在本地项目里新建一个 Dockerfile 用于之后创建镜像</p>
<h2>创建 Dockerfile</h2>
<p>当云服务器接收到项目更新后发送的 post 请求后，需要创建/更新镜像来实现自动化部署</p>
<h1>处理项目更新的请求</h1>
<p>参数主要涉及当前仓库和本地提交的信息，这里我们只用 <code>repository.name</code> 获取更新的仓库名即可</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2074" data-height="1620"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-e637f9d0a04e0c11" data-original-width="2074" data-original-height="1620" data-original-format="image/png" data-original-filesize="268946" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>配置完成后，可以向仓库提交一个 commit，然后点击最下方可以看到 post 请求参数</p>
<h2>测试 webhook</h2>
<p>点击 <code>Add webhook</code> 为当前项目添加一个 webhook，至此，当 <code>docker-test</code> 项目有代码提交时，就会往 <code>http://118.89.244.45:3000</code> 发送一个 post 请求</p>
<p>webhook 还可以设置一些鉴权相关的 token，由于是个人项目这里不详细展开了</p>
<ul>
<li><p>触发时机：Just the push event，即仓库 push 事件，根据不同的需求还可以选择其他事件，例如 PR，提交 Commit，提交 issues 等</p></li>
<li><p>Content type：选择 application/json 即发送 json 格式的 post 请求</p></li>
<li><p>Payload URL：填写云服务器公网 IP，记得添加 http(s) 前缀</p></li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1888" data-height="1256"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-b415b6e2bd9e103b" data-original-width="1888" data-original-height="1256" data-original-format="image/png" data-original-filesize="162916" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="3130" data-height="1378"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-b552bf85bacc6d2e" data-original-width="3130" data-original-height="1378" data-original-format="image/png" data-original-filesize="235402" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>打开 github 的仓库主页，点击右侧 settings</p>
<h2>配置 webhook</h2>
<p><code>当仓库有提交代码时，通过将 webhook 请求地址指向云服务器 IP 地址，云服务器就能知道项目有更新，之后运行相关代码实现自动化部署</code></p>
<p>参考 Vue 生命周期，当组件挂载完成时会触发 mounted 钩子，在钩子中可以编写拉取后端数据，或者渲染页面等回调逻辑，而 github 的 webhook 会在当前仓库触发某些事件时，发送一个 post 形式的 http 请求</p>
<p>hook 翻译为“钩子”，还可以理解为“回调”</p>
<h1>webhook</h1>
<p>并将 demo 项目上传到 github，准备配置 webhook</p>
<p>简单使用 vue-cli 在本地创建项目</p>
<h1>创建 demo 项目</h1>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="6138" data-height="1493"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-bd2deb5af2a2299b" data-original-width="6138" data-original-height="1493" data-original-format="image/png" data-original-filesize="107761" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>node 安装完成后，还需要安装 <code>pm2</code>，它能使你的 js 脚本能在云服务器的后台运行</p>
<p>通过 nvm 安装最新版 node</p>
<p>将 nvm 作为环境变量</p>
<p>既然是前端自动化部署，云服务器上相关处理逻辑用 js 编写，所以需要安装 node 环境，这里用 nvm 来管理 node 版本</p>
<h3>node</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="814" data-height="462"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-e0a3e8794b88188e.jpg" data-original-width="814" data-original-height="462" data-original-format="image/jpeg" data-original-filesize="49449" src="https://upload-images.jianshu.io/upload_images/13835400-e0a3e8794b88188e.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image-20200630125450964</div>
</div>
<p>由于 SSH 方式还需要在 github 上注册公钥，方便起见，之后会选择 HTTPS 的方式克隆仓库</p>
<p>自动化部署涉及到拉取最新的代码，所以需要安装 git 环境</p>
<h3>git</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="946" data-height="420"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-74db2f8f9462a08b" data-original-width="946" data-original-height="420" data-original-format="image/png" data-original-filesize="255096" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>弹出 <code>Hello from Docker!</code> 证明 Docker 已经成功安装啦～</p>
<p>云服务器安装和本地有些区别，根据 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.docker.com%2Fengine%2Finstall%2Fcentos%2F" target="_blank">docker 官网</a> 的安装教程，运行以下命令</p>
<p>之前在本地安装了 docker，但云服务器上默认也是没有的，所以需要给它也安装 docker 环境</p>
<h3>docker</h3>
<p>接着给云服务器安装基础的环境</p>
<h2>安装环境</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="754" data-height="266"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-06ba9733d879a312" data-original-width="754" data-original-height="266" data-original-format="image/png" data-original-filesize="177331" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>绑定完成后重新开机，至此就可以在本地通过 ssh 命令登陆云服务器啦</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2358" data-height="1468"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-9aef335f755e830b" data-original-width="2358" data-original-height="1468" data-original-format="image/png" data-original-filesize="183085" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>除了注册公钥，还需要将它绑定实例，将<code>实例关机并进行绑定</code></p>
<p>将生成的公钥放在云服务器控制台图示部分，点击确定</p>
<p>没有生成过密钥本地运行以下命令即可，参考 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgit-scm.com%2Fbook%2Fzh%2Fv2%2F%25E6%259C%258D%25E5%258A%25A1%25E5%2599%25A8%25E4%25B8%258A%25E7%259A%2584-Git-%25E7%2594%259F%25E6%2588%2590-SSH-%25E5%2585%25AC%25E9%2592%25A5" target="_blank">服务器上的 Git - 生成 SSH 公钥</a></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="754" data-height="418"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-ebdc38a2ba30a156" data-original-width="754" data-original-height="418" data-original-format="image/png" data-original-filesize="362014" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>生成密钥的方式同 git，之前生成过的话本地执行以下命令就能查看</p>
<p></p>
<p></p>
前者无需配置，但每次登陆都需要输入账号密码，后者需要注册 ssh 密钥，但之后可以免密登陆云服务器。个人比较喜欢后者，所以先在控制台注册 ssh 密钥  <div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2656" data-height="1420"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-32d83f853b5a5746" data-original-width="2656" data-original-height="1420" data-original-format="image/png" data-original-filesize="285141" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>然后我们需要登陆云服务器，本地登陆云服务器的方式一般有两种，密码登陆和 ssh 登陆（或者用 ssh 工具，windows 系统可以用 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fbaike.baidu.com%2Fitem%2FXshell%2F5659054" target="_blank">xhell</a>，macOS 可以用 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.putty.org%2F" target="_blank">putty</a>）</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="3304" data-height="1576"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-06cb1ac0240510b1" data-original-width="3304" data-original-height="1576" data-original-format="image/png" data-original-filesize="356270" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>公网 IP 用于之后 webhook 发送请求的地址</p>
<p>注册相关的操作不细说了，参考供应商教程，随后登陆控制台可以看到当前云服务器的公网 IP，例如下图中服务器的公网 IP 是：118.89.244.45</p>
<p><code>熟悉云服务器配置或者不是腾讯云的读者可以跳过这章</code></p>
<h2>登陆云服务器</h2>
<p>由于是个人项目，对云服务器的要求不高，大部分供应商会给新用户<del>白嫖</del>免费试用 1-2 周，这里我选择腾讯云 <code>CentOS 7.6 64位</code> 的操作系统，当然阿里云或其他云服务器也完全 ok</p>
<p>首先你得有一台服务器吧-。-</p>
<h1>云服务器</h1>
<p>可以发现，实现前端自动化部署后开发者需要做的只是把代码推到仓库，其余的事都可以通过服务器上的自动化脚本完成</p>
<ul>
<li><p><code>git push</code> 提交代码到仓库</p></li>
<li><p>服务器自动更新镜像</p></li>
<li><p>镜像中自动运行 <code>npm run build</code> 生成构建产物</p></li>
<li><p>服务器自动创建容器</p></li>
</ul>
<p>在实现前端自动化部署后：</p>
<ul>
<li><p>本地运行 <code>npm run build</code> 生成构建产物</p></li>
<li><p>将产物通过 ftp 等形式上传到服务器</p></li>
<li><p><code>git push</code> 提交代码到仓库</p></li>
</ul>
<p>在没迁移 Docker 之前，若我想更新线上网站中内容时，需要：</p>
<p>介绍完 docker，接着我们从零开始实现前端自动化部署</p>
<h1>前端自动化部署</h1>
<p>相比于真实服务器/虚拟机，容器不包含操作系统，这意味着创建/销毁容器都十分高效</p>
<h3>高效并节省资源</h3>
<p>使用 docker 可以使你的服务器更干净，构建用到的环境可以都放在容器中</p>
<h3>环境隔离</h3>
<p>在创建镜像时可以使用 tag 标记版本，如果某个版本的环境有问题，可以快速回滚到之前版本</p>
<p>类似 git，docker 也有版本控制</p>
<h3>便于回滚</h3>
<p>服务器拉取账号 <code>yeyan1996</code> 下的 <code>docker-test-image</code> 镜像</p>
<blockquote>
<p>docker pull yeyan1996/docker-test-image:latest</p>
</blockquote>
<p>本地提交名为 <code>docker-test-image</code> 的镜像，镜像名需要加上 dockerhub 账号作为前缀</p>
<blockquote>
<p>docker push yeyan1996/docker-test-image:latest</p>
</blockquote>
<p>开发者可以将开发环境用 docker 镜像上传到 docker 仓库，在生产环境拉取并运行相同的镜像，保持环境一致</p>
<p>docker 的出现解决了一个世纪难题：<code>在我电脑上明明是好的</code> :)</p>
<h3>环境统一</h3>
<p>有人会问，环境我都可以装在自己的服务器上，为什么还要放在一个个容器里呢？这里列举使用 docker 的几个优点</p>
<p>了解了 docker 的概念和使用方法，接着讲讲为什么要用 docker</p>
<h2>为什么要用 docker</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2294" data-height="700"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-48e2eaf77e6a97a6" data-original-width="2294" data-original-height="700" data-original-format="image/png" data-original-filesize="125181" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>由于上一步操作本地 80 端口已经被占用了，这里使用 81 端口映射到容器的 80 端口，访问 <code>localhost:81</code> 可以看到 nginx 启动页面</p>
<p>第一步拉取了官方的 nginx 镜像，第二步用基于官方 nginx 镜像创建名为 <code>nginx-container</code> 的容器</p>
<p>开发者可以将 Dockerfile 生成的镜像上传到 dockerhub 来存储自定义镜像，也可以直接使用官方提供的镜像</p>
<p>如果说 github 是存储代码的仓库，那么 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fhub.docker.com%2F" target="_blank">dockerhub</a> 就是存储镜像的仓库</p>
<h2>DockerHub</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="686" data-height="258"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-a92a90b150677083" data-original-width="686" data-original-height="258" data-original-format="image/png" data-original-filesize="16869" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>由于本地 80 端口映射到了容器的 80 端口，所以当输入 <code>localhost</code> 时，会显示 index.html 文件内容</p>
<ul>
<li><p>run：创建并运行 docker 容器</p></li>
<li><p>-d： 后台运行容器</p></li>
<li><p>80:80：将当前服务器的 80 端口（冒号前的 80），映射到容器的 80 端口（冒号后的 80）</p></li>
<li><p>--name：给容器命名，便于之后定位容器</p></li>
<li><p>test-image:latest：基于 <code>test-image</code> 最新版本的镜像创建容器</p></li>
</ul>
<p>镜像成功创建后，运行以下命令可以创建一个 docker 容器</p>
<h3>创建容器</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1000" data-height="474"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-673a7fe266fcc136" data-original-width="1000" data-original-height="474" data-original-format="image/png" data-original-filesize="66261" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<ul>
<li><p>build：创建 docker 镜像</p></li>
<li><p>.：使用当前目录下的 dockerfile 文件</p></li>
<li><p>-t：使用 tag 标记版本</p></li>
<li><p>test-image:latest：创建名为 <code>test-image</code> 的镜像，并标记为 latest（最新）版本</p></li>
</ul>
<p>在创建 Dockerfile 文件后，在当前目录运行以下命令可以创建一个 docker 镜像</p>
<h3>创建镜像</h3>
<p>此时，你的文件结构应该是</p>
<p>其他 Dockerfile 配置参考<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.docker.com%2Fengine%2Freference%2Fbuilder%2F%23from" target="_blank">官方文档</a></p>
<ul>
<li><p>FROM nginx：基于官方 nginx 镜像</p></li>
<li><p>COPY index.html /usr/share/nginx/html/index.html：<strong>将当前目录下 index.html 替换容器中 /usr/share/nginx/html/index.html 文件， <code>/usr/share/nginx/html</code> 是 nginx 默认存放网页文件的目录，访问容器 80 端口会展示该目录下 index.html 文件</strong></p></li>
<li><p>EXPOSE 80：容器对外暴露 80 端口，主要起声明作用，真实端口映射还需要在创建容器时定义</p></li>
</ul>
<p>首先创建一个 <code>hello-docker</code> 目录，在目录中创建 <code>index.html</code> 和 <code>Dockerfile</code> 文件</p>
<h3>创建文件</h3>
<p>尝试用 Dockerfile 创建 docker 镜像</p>
<p>Dockerfile 是一个配置文件，类似 .gitlab-ci.yml/package.json，定义了如何生成镜像</p>
<h2>Dockerfile</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1404" data-height="567"><img data-original-src="//upload-images.jianshu.io/upload_images/13835400-1f41650516112f13" data-original-width="1404" data-original-height="567" data-original-format="image/png" data-original-filesize="79118" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<ul>
<li><p>Dockerfile 文件创建而成</p></li>
<li><p>直接使用 DockerHub 或者其他仓库上现有的镜像</p></li>
</ul>
<p>有两种方式获取镜像</p>
<p>如果把容器比作轻量的服务器，那么镜像就是创建它的模版，一个 docker 镜像可以创建多个容器，它们的关系好比 JavaScript 中类和实例的关系</p>
<ul>
<li><p>镜像（image）</p></li>
<li><p>容器（container）</p></li>
<li><p>仓库（repository）</p></li>
</ul>
<p>docker 有三个重要的概念</p>
<h2>基本概念</h2>
  
</div>
            