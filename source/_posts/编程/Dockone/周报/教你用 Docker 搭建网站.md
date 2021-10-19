
---
title: '教你用 Docker 搭建网站'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/c4d5449531b08a2f703c2405e948ba32.png'
author: Dockone
comments: false
date: 2021-10-19 15:08:12
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/c4d5449531b08a2f703c2405e948ba32.png'
---

<div>   
<br>2013 年发布至今，  <a href="https://www.docker.com/">Docker</a>  一直广受瞩目，被认为可能会改变软件行业。<br>
<br>但是，许多人并不清楚 Docker 到底是什么，要解决什么问题，好处又在哪里？本文就来详细解释，帮助大家理解它，还带有简单易懂的实例，教你如何将它用于日常开发。<br>
<h3>环境配置的难题</h3>软件开发最大的麻烦事之一，就是环境配置。用户计算机的环境都不相同，你怎么知道自家的软件，能在那些机器跑起来？<br>
<br>用户必须保证两件事：操作系统的设置，各种库和组件的安装。只有它们都正确，软件才能运行。举例来说，安装一个 Python 应用，计算机必须有 Python 引擎，还必须有各种依赖，可能还要配置环境变量。<br>
<br>如果某些老旧的模块与当前环境不兼容，那就麻烦了。开发者常常会说："它在我的机器可以跑了"（It works on my machine），言下之意就是，其他机器很可能跑不了。<br>
<br>环境配置如此麻烦，换一台机器，就要重来一次，旷日费时。很多人想到，能不能从根本上解决问题，软件可以带环境安装？也就是说，安装的时候，把原始环境一模一样地复制过来。<br>
<h3>虚拟机</h3>虚拟机（virtual machine）就是带环境安装的一种解决方案。它可以在一种操作系统里面运行另一种操作系统，比如在 Windows 系统里面运行 Linux 系统。应用程序对此毫无感知，因为虚拟机看上去跟真实系统一模一样，而对于底层系统来说，虚拟机就是一个普通文件，不需要了就删掉，对其他部分毫无影响。<br>
<br>虽然用户可以通过虚拟机还原软件的原始环境。但是，这个方案有几个缺点：<br>
<ul><li>资源占用多，虚拟机会独占一部分内存和硬盘空间。它运行的时候，其他程序就不能使用这些资源了。哪怕虚拟机里面的应用程序，真正使用的内存只有 1MB，虚拟机依然需要几百 MB 的内存才能运行。</li><li>冗余步骤多，虚拟机是完整的操作系统，一些系统级别的操作步骤，往往无法跳过，比如用户登录。</li><li>启动慢，启动操作系统需要多久，启动虚拟机就需要多久。可能要等几分钟，应用程序才能真正运行。</li></ul><br>
<br><h3>Linux 容器</h3>由于虚拟机存在这些缺点，Linux 发展出了另一种虚拟化技术：Linux 容器（Linux Containers，缩写为 LXC）。<br>
<br><strong>Linux 容器不是模拟一个完整的操作系统，而是对进程进行隔离</strong>。或者说，在正常进程的外面套了一个<a href="https://opensource.com/article/18/1/history-low-level-container-runtimes">保护层</a>。对于容器里面的进程来说，它接触到的各种资源都是虚拟的，从而实现与底层系统的隔离。<br>
<br>由于容器是进程级别的，相比虚拟机有很多优势。<br>
<ul><li>启动快，容器里面的应用，直接就是底层系统的一个进程，而不是虚拟机内部的进程。所以，启动容器相当于启动本机的一个进程，而不是启动一个操作系统，速度就快很多。</li><li>资源占用少，容器只占用需要的资源，不占用那些没有用到的资源；虚拟机由于是完整的操作系统，不可避免要占用所有资源。另外，多个容器可以共享资源，虚拟机都是独享资源。</li><li>体积小，容器只要包含用到的组件即可，而虚拟机是整个操作系统的打包，所以容器文件比虚拟机文件要小很多。</li></ul><br>
<br>总之，容器有点像轻量级的虚拟机，能够提供虚拟化的环境，但是成本开销小得多。<br>
<h3>Docker 是什么？</h3><strong>Docker 属于 Linux 容器的一种封装，提供简单易用的容器使用接口</strong>。它是目前最流行的 Linux 容器解决方案。<br>
<br>Docker 将应用程序与该程序的依赖，打包在一个文件里面。运行这个文件，就会生成一个虚拟容器。程序在这个虚拟容器里运行，就好像在真实的物理机上运行一样。有了 Docker，就不用担心环境问题。<br>
<br>总体来说，Docker 的接口相当简单，用户可以方便地创建和使用容器，把自己的应用放入容器。容器还可以进行版本管理、复制、分享、修改，就像管理普通的代码一样。<br>
<h3>Docker 的用途</h3>Docker 的主要用途，目前有三大类。<br>
<ul><li>提供一次性的环境。比如，本地测试他人的软件、持续集成的时候提供单元测试和构建的环境。</li><li>提供弹性的云服务。因为 Docker 容器可以随开随关，很适合动态扩容和缩容。</li><li>组建微服务架构。通过多个容器，一台机器可以跑多个服务，因此在本机就可以模拟出微服务架构。</li></ul><br>
<br><h3>Docker 的安装</h3>Docker 是一个开源的商业产品，有两个版本：社区版（Community Edition，缩写为 CE）和企业版（Enterprise Edition，缩写为 EE）。企业版包含了一些收费服务，个人开发者一般用不到。下面的介绍都针对社区版。<br>
<br>Docker CE 的安装请参考官方文档。<br>
<ul><li><a href="https://docs.docker.com/docker-for-mac/install/">Mac</a></li><li><a href="https://docs.docker.com/docker-for-windows/install/">Windows</a></li><li><a href="https://docs.docker.com/install/linux/docker-ce/ubuntu/">Ubuntu</a></li><li><a href="https://docs.docker.com/install/linux/docker-ce/debian/">Debian</a></li><li><a href="https://docs.docker.com/install/linux/docker-ce/centos/">CentOS</a></li><li><a href="https://docs.docker.com/install/linux/docker-ce/fedora/">Fedora</a></li><li><a href="https://docs.docker.com/install/linux/docker-ce/binaries/">其他 Linux 发行版</a></li></ul><br>
<br>安装完成后，运行下面的命令，验证是否安装成功。<br>
<pre class="prettyprint">$ docker version<br>
# 或者<br>
$ docker info<br>
</pre><br>
Docker 需要用户具有 sudo 权限，为了避免每次命令都输入 <code class="prettyprint">sudo</code>，可以把用户加入 Docker 用户组（<a href="https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user">官方文档</a>）。<br>
<pre class="prettyprint">$ sudo usermod -aG docker $USER<br>
</pre><br>
Docker 是服务器----客户端架构。命令行运行 <code class="prettyprint">docker</code> 命令的时候，需要本机有 Docker 服务。如果这项服务没有启动，可以用下面的命令启动（<a href="https://docs.docker.com/config/daemon/systemd/">官方文档</a>）。<br>
<pre class="prettyprint"># service 命令的用法<br>
$ sudo service docker start<br>
<br>
# systemctl 命令的用法<br>
$ sudo systemctl start docker<br>
</pre><br>
<h3>image 文件</h3><strong>Docker 把应用程序及其依赖，打包在 image 文件里面</strong>。只有通过这个文件，才能生成 Docker 容器。image 文件可以看作是容器的模板。Docker 根据 image 文件生成容器的实例。同一个 image 文件，可以生成多个同时运行的容器实例。<br>
<br>image 是二进制文件。实际开发中，一个 image 文件往往通过继承另一个 image 文件，加上一些个性化设置而生成。举例来说，你可以在 Ubuntu 的 image 基础上，往里面加入 Apache 服务器，形成你的 image。<br>
<pre class="prettyprint"># 列出本机的所有 image 文件。<br>
$ docker image ls<br>
<br>
# 删除 image 文件<br>
$ docker image rm [imageName] <br>
</pre><br>
image 文件是通用的，一台机器的 image 文件拷贝到另一台机器，照样可以使用。一般来说，为了节省时间，我们应该尽量使用别人制作好的 image 文件，而不是自己制作。即使要定制，也应该基于别人的 image 文件进行加工，而不是从零开始制作。<br>
<br>为了方便共享，image 文件制作完成后，可以上传到网上的仓库。Docker 的官方仓库 <a href="https://hub.docker.com/">Docker Hub</a> 是最重要、最常用的 image 仓库。此外，出售自己制作的 image 文件也是可以的。<br>
<h3>实例：hello world</h3>下面，我们通过最简单的 image 文件“<a href="https://hub.docker.com/r/library/hello-world/">hello world</a>”，感受一下 Docker。<br>
<br>首先，运行下面的命令，将 image 文件从仓库抓取到本地。<br>
<pre class="prettyprint">$ docker image pull library/hello-world<br>
</pre><br>
上面代码中，<code class="prettyprint">docker image pull</code> 是抓取 image 文件的命令。<code class="prettyprint">library/hello-world</code> 是 image 文件在仓库里面的位置，其中 <code class="prettyprint">library</code> 是 image 文件所在的组，<code class="prettyprint">hello-world</code> 是 image 文件的名字。<br>
<br>由于 Docker 官方提供的 image 文件，都放在 <a href="https://hub.docker.com/r/library/">library</a> 组里面，所以它的是默认组，可以省略。因此，上面的命令可以写成下面这样。<br>
<pre class="prettyprint">$ docker image pull hello-world<br>
</pre><br>
抓取成功以后，就可以在本机看到这个 image 文件了。<br>
<pre class="prettyprint">$ docker image ls<br>
</pre><br>
现在，运行这个 image 文件。<br>
<pre class="prettyprint">$ docker container run hello-world<br>
</pre><br>
<code class="prettyprint">docker container run</code> 命令会从 image 文件，生成一个正在运行的容器实例。<br>
<br>注意，<code class="prettyprint">docker container run</code> 命令具有自动抓取 image 文件的功能。如果发现本地没有指定的 image 文件，就会从仓库自动抓取。因此，前面的 <code class="prettyprint">docker image pull</code> 命令并不是必需的步骤。<br>
<br>如果运行成功，你会在屏幕上读到下面的输出。<br>
<pre class="prettyprint">$ docker container run hello-world<br>
<br>
Hello from Docker!<br>
This message shows that your installation appears to be working correctly.<br>
<br>
... ...<br>
</pre><br>
输出这段提示以后，<code class="prettyprint">hello world</code> 就会停止运行，容器自动终止。<br>
<br>有些容器不会自动终止，因为提供的是服务。比如，安装运行 Ubuntu 的 image，就可以在命令行体验 Ubuntu 系统。<br>
<pre class="prettyprint">$ docker container run -it ubuntu bash<br>
</pre><br>
对于那些不会自动终止的容器，必须使用 <a href="https://docs.docker.com/engine/reference/commandline/container_kill/">docker container kill</a> 命令手动终止。<br>
<pre class="prettyprint">$ docker container kill [containID]<br>
</pre><br>
<h3>容器文件</h3><strong>image 文件生成的容器实例，本身也是一个文件，称为容器文件</strong>。也就是说，一旦容器生成，就会同时存在两个文件： image 文件和容器文件。而且关闭容器并不会删除容器文件，只是容器停止运行而已。<br>
<pre class="prettyprint"># 列出本机正在运行的容器<br>
$ docker container ls<br>
<br>
# 列出本机所有容器，包括终止运行的容器<br>
$ docker container ls --all<br>
</pre><br>
上面命令的输出结果之中，包括容器的 ID。很多地方都需要提供这个 ID，比如上一节终止容器运行的 <code class="prettyprint">docker container kill</code> 命令。<br>
<br>终止运行的容器文件，依然会占据硬盘空间，可以使用 <a href="https://docs.docker.com/engine/reference/commandline/container_rm/">docker container rm</a> 命令删除。<br>
<pre class="prettyprint">$ docker container rm [containerID] <br>
</pre><br>
运行上面的命令之后，再使用 <code class="prettyprint">docker container ls --all</code> 命令，就会发现被删除的容器文件已经消失了。<br>
<h3>Dockerfile 文件</h3>学会使用 image 文件以后，接下来的问题就是，如何可以生成 image 文件？如果你要推广自己的软件，势必要自己制作 image 文件。<br>
<br>这就需要用到 Dockerfile 文件。它是一个文本文件，用来配置 image。Docker 根据 该文件生成二进制的 image 文件。<br>
<br>下面通过一个实例，演示如何编写 Dockerfile 文件。<br>
<h3>实例：制作自己的 Docker 容器</h3>下面我以 <a href="https://www.ruanyifeng.com/blog/2017/08/koa.html">koa-demos</a> 项目为例，介绍怎么写 Dockerfile 文件，实现让用户在 Docker 容器里面运行 Koa 框架。<br>
<br>作为准备工作，请先 <a href="https://github.com/ruanyf/koa-demos/archive/master.zip">下载源码</a>。<br>
<pre class="prettyprint">$ git clone https://github.com/ruanyf/koa-demos.git<br>
$ cd koa-demos<br>
</pre><br>
<h4>编写 Dockerfile 文件</h4>首先，在项目的根目录下，新建一个文本文件 <code class="prettyprint">.dockerignore</code>，写入下面的 <a href="https://github.com/ruanyf/koa-demos/blob/master/.dockerignore">内容</a>。<br>
<pre class="prettyprint">.git<br>
node_modules<br>
npm-debug.log<br>
</pre><br>
上面代码表示，这三个路径要排除，不要打包进入 image 文件。如果你没有路径要排除，这个文件可以不新建。<br>
<br>然后，在项目的根目录下，新建一个文本文件 Dockerfile，写入下面的 <a href="https://github.com/ruanyf/koa-demos/blob/master/Dockerfile">内容</a>。<br>
<pre class="prettyprint">FROM node:8.4<br>
COPY . /app<br>
WORKDIR /app<br>
RUN npm install --registry=https://registry.npm.taobao.org<br>
EXPOSE 3000<br>
</pre><br>
上面代码一共五行，含义如下。<br>
<ul><li><code class="prettyprint">FROM node:8.4</code>：该 image 文件继承官方的 node image，冒号表示标签，这里标签是 <code class="prettyprint">8.4</code>，即 8.4 版本的 Node。</li><li><code class="prettyprint">COPY . /app</code>：将当前目录下的所有文件（除了 <code class="prettyprint">.dockerignore</code> 排除的路径），都拷贝进入 image 文件的 <code class="prettyprint">/app</code> 目录。</li><li><code class="prettyprint">WORKDIR /app</code>：指定接下来的工作路径为 <code class="prettyprint">/app</code>。</li><li><code class="prettyprint">RUN npm install</code>：在 <code class="prettyprint">/app</code> 目录下，运行 <code class="prettyprint">npm install</code> 命令安装依赖。注意，安装后所有的依赖，都将打包进入 image 文件。</li><li><code class="prettyprint">EXPOSE 3000</code>：将容器 3000 端口暴露出来， 允许外部连接这个端口。</li></ul><br>
<br><h4>创建 image 文件</h4>有了 Dockerfile 文件以后，就可以使用 <code class="prettyprint">docker image build</code> 命令创建 image 文件了。<br>
<pre class="prettyprint">$ docker image build -t koa-demo .<br>
# 或者<br>
$ docker image build -t koa-demo:0.0.1 .<br>
</pre><br>
上面代码中，<code class="prettyprint">-t</code> 参数用来指定 image 文件的名字，后面还可以用冒号指定标签。如果不指定，默认的标签就是 <code class="prettyprint">latest</code>。最后的那个点表示 Dockerfile 文件所在的路径，上例是当前路径，所以是一个点。<br>
<br>如果运行成功，就可以看到新生成的 image 文件 <code class="prettyprint">koa-demo</code> 了。<br>
<pre class="prettyprint">$ docker image ls<br>
</pre><br>
<h4>生成容器</h4><code class="prettyprint">docker container run</code> 命令会从 image 文件生成容器。<br>
<pre class="prettyprint">$ docker container run -p 8000:3000 -it koa-demo /bin/bash<br>
# 或者<br>
$ docker container run -p 8000:3000 -it koa-demo:0.0.1 /bin/bash<br>
</pre><br>
上面命令的各个参数含义如下：<br>
<ul><li><code class="prettyprint">-p</code> 参数：容器的 3000 端口映射到本机的 8000 端口。</li><li><code class="prettyprint">-it</code> 参数：容器的 Shell 映射到当前的 Shell，然后你在本机窗口输入的命令，就会传入容器。</li><li><code class="prettyprint">koa-demo:0.0.1</code>：image 文件的名字（如果有标签，还需要提供标签，默认是 latest 标签）。</li><li><code class="prettyprint">/bin/bash</code>：容器启动以后，内部第一个执行的命令。这里是启动 Bash，保证用户可以使用 Shell。</li></ul><br>
<br>如果一切正常，运行上面的命令以后，就会返回一个命令行提示符。<br>
<pre class="prettyprint">root@66d80f4aaf1e:/app#<br>
</pre><br>
这表示你已经在容器里面了，返回的提示符就是容器内部的 Shell 提示符。执行下面的命令。<br>
<pre class="prettyprint">root@66d80f4aaf1e:/app# node demos/01.js<br>
</pre><br>
这时，Koa 框架已经运行起来了。打开本机的浏览器，访问 <a href="http://127.0.0.1:8000/" rel="nofollow" target="_blank">http://127.0.0.1:8000</a>，网页显示“Not Found”，这是因为这个 <a href="https://github.com/ruanyf/koa-demos/blob/master/demos/01.js">demo</a> 没有写路由。<br>
<br>这个例子中，Node 进程运行在 Docker 容器的虚拟环境里面，进程接触到的文件系统和网络接口都是虚拟的，与本机的文件系统和网络接口是隔离的，因此需要定义容器与物理机的端口映射（map）。<br>
<br>现在，在容器的命令行，按下 Ctrl + c 停止 Node 进程，然后按下 Ctrl + d （或者输入 exit）退出容器。此外，也可以用 <code class="prettyprint">docker container kill</code> 终止容器运行。<br>
<pre class="prettyprint"># 在本机的另一个终端窗口，查出容器的 ID<br>
$ docker container ls<br>
<br>
# 停止指定的容器运行<br>
$ docker container kill [containerID] <br>
</pre><br>
容器停止运行之后，并不会消失，用下面的命令删除容器文件。<br>
<pre class="prettyprint"># 查出容器的 ID<br>
$ docker container ls --all<br>
<br>
# 删除指定的容器文件<br>
$ docker container rm [containerID] <br>
</pre><br>
也可以使用 <code class="prettyprint">docker container run</code> 命令的 <code class="prettyprint">--rm</code> 参数，在容器终止运行后自动删除容器文件。<br>
<pre class="prettyprint">$ docker container run --rm -p 8000:3000 -it koa-demo /bin/bash<br>
</pre><br>
<h4>CMD 命令</h4>上一节的例子里面，容器启动以后，需要手动输入命令 <code class="prettyprint">node demos/01.js</code>。我们可以把这个命令写在 Dockerfile 里面，这样容器启动以后，这个命令就已经执行了，不用再手动输入了。<br>
<pre class="prettyprint">FROM node:8.4<br>
COPY . /app<br>
WORKDIR /app<br>
RUN npm install --registry=https://registry.npm.taobao.org<br>
EXPOSE 3000<br>
CMD node demos/01.js<br>
</pre><br>
上面的 Dockerfile 里面，多了最后一行 <code class="prettyprint">CMD node demos/01.js</code>，它表示容器启动后自动执行 <code class="prettyprint">node demos/01.js</code>。<br>
<br>你可能会问，<code class="prettyprint">RUN</code> 命令与 <code class="prettyprint">CMD</code> 命令的区别在哪里？简单说，<code class="prettyprint">RUN</code> 命令在 image 文件的构建阶段执行，执行结果都会打包进入 image 文件；<code class="prettyprint">CMD</code> 命令则是在容器启动后执行。另外，一个 Dockerfile 可以包含多个 <code class="prettyprint">RUN</code> 命令，但是只能有一个 <code class="prettyprint">CMD</code> 命令。<br>
<br>注意，指定了 <code class="prettyprint">CMD</code> 命令以后，<code class="prettyprint">docker container run</code> 命令就不能附加命令了（比如前面的 <code class="prettyprint">/bin/bash</code>），否则它会覆盖 <code class="prettyprint">CMD</code> 命令。现在，启动容器可以使用下面的命令。<br>
<pre class="prettyprint">$ docker container run --rm -p 8000:3000 -it koa-demo:0.0.1<br>
</pre><br>
<h4>发布 image 文件</h4>容器运行成功后，就确认了 image 文件的有效性。这时，我们就可以考虑把 image 文件分享到网上，让其他人使用。<br>
<br>首先，去 <a href="https://hub.docker.com/">hub.docker.com</a> 或 <a href="https://cloud.docker.com/">cloud.docker.com</a> 注册一个账户。然后，用下面的命令登录。<br>
<pre class="prettyprint">$ docker login<br>
</pre><br>
接着，为本地的 image 标注用户名和版本。<br>
<pre class="prettyprint">$ docker image tag [imageName] [username]/[repository]:[tag]<br>
# 实例<br>
$ docker image tag koa-demos:0.0.1 ruanyf/koa-demos:0.0.1<br>
</pre><br>
也可以不标注用户名，重新构建一下 image 文件。<br>
<pre class="prettyprint">$ docker image build -t [username]/[repository]:[tag] .<br>
</pre><br>
最后，发布 image 文件。<br>
<pre class="prettyprint">$ docker image push [username]/[repository]:[tag]<br>
</pre><br>
发布成功以后，登录 hub.docker.com，就可以看到已经发布的 image 文件。<br>
<h3>其他有用的命令</h3>Docker 的主要用法就是上面这些，此外还有几个命令，也非常有用。<br>
<h4>docker container start</h4>前面的 <code class="prettyprint">docker container run</code> 命令是新建容器，每运行一次，就会新建一个容器。同样的命令运行两次，就会生成两个一模一样的容器文件。如果希望重复使用容器，就要使用 <code class="prettyprint">docker container start</code> 命令，它用来启动已经生成、已经停止运行的容器文件。<br>
<pre class="prettyprint">$ docker container start [containerID] <br>
</pre><br>
<h4>docker container stop</h4>前面的 <code class="prettyprint">docker container kill</code> 命令终止容器运行，相当于向容器里面的主进程发出 SIGKILL 信号。而 <code class="prettyprint">docker container stop</code> 命令也是用来终止容器运行，相当于向容器里面的主进程发出 SIGTERM 信号，然后过一段时间再发出 SIGKILL 信号。<br>
<pre class="prettyprint">$ docker container stop [containerID] <br>
</pre><br>
这两个信号的差别是，应用程序收到 SIGTERM 信号以后，可以自行进行收尾清理工作，但也可以不理会这个信号。如果收到 SIGKILL 信号，就会强行立即终止，那些正在进行中的操作会全部丢失。<br>
<h4>docker container logs</h4><code class="prettyprint">docker container logs</code> 命令用来查看 Docker 容器的输出，即容器里面 Shell 的标准输出。如果 <code class="prettyprint">docker run</code> 命令运行容器的时候，没有使用 <code class="prettyprint">-it</code> 参数，就要用这个命令查看输出。<br>
<pre class="prettyprint">$ docker container logs [containerID] <br>
</pre><br>
<h4>docker container exec</h4><code class="prettyprint">docker container exec</code> 命令用于进入一个正在运行的 Docker 容器。如果 <code class="prettyprint">docker run</code> 命令运行容器的时候，没有使用 <code class="prettyprint">-it</code> 参数，就要用这个命令进入容器。一旦进入了容器，就可以在容器的 Shell 执行命令了。<br>
<pre class="prettyprint">$ docker container exec -it [containerID] /bin/bash<br>
</pre><br>
<h4>docker container cp</h4><code class="prettyprint">docker container cp</code> 命令用于从正在运行的 Docker 容器里面，将文件拷贝到本机。下面是拷贝到当前目录的写法。<br>
<pre class="prettyprint">$ docker container cp [containID]:[/path/to/file] . <br>
</pre><br>
Docker 是一个容器工具，提供虚拟环境。很多人认为，它改变了我们对软件的认识。<br>
<br>站在 Docker 的角度，软件就是容器的组合：业务逻辑容器、数据库容器、储存容器、队列容器......Docker 使得软件可以拆分成若干个标准化容器，然后像搭积木一样组合起来。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/c4d5449531b08a2f703c2405e948ba32.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/c4d5449531b08a2f703c2405e948ba32.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这正是微服务（microservices）的思想：软件把任务外包出去，让各种外部服务完成这些任务，软件本身只是底层服务的调度中心和组装层。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/ce8b44b73982afd5451ae2493171da26.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/ce8b44b73982afd5451ae2493171da26.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
微服务很适合用 Docker 容器实现，每个容器承载一个服务。一台计算机同时运行多个容器，从而就能很轻松地模拟出复杂的微服务架构。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/4868e20c794a2e07f359d9d665da6526.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/4868e20c794a2e07f359d9d665da6526.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
之前的内容介绍了 Docker 的概念和基本用法，接着往下介绍，如何在一台计算机上实现多个服务，让它们互相配合，组合出一个应用程序。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/73aced8b7c5d95f0a09cb474a20b2b91.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/73aced8b7c5d95f0a09cb474a20b2b91.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我选择的示例软件是 <a href="https://wordpress.org/">WordPress</a>。它是一个常用软件，全世界用户据说超过几千万。同时它又非常简单，只要两个容器就够了（业务容器 + 数据库容器），很适合教学。而且，这种"业务 + 数据库"的容器架构，具有通用性，许多应用程序都可以复用。<br>
<br>为了加深读者理解，本文采用三种方法，演示如何架设 WordPress 网站。<br>
<ul><li>方法 A：自建 WordPress 容器</li><li>方法 B：采用官方的 WordPress 容器</li><li>方法 C：采用 Docker Compose 工具</li></ul><br>
<br><h3>预备工作：image 仓库的镜像网址</h3>本教程需要从仓库下载 image 文件，但是国内访问 Docker 的官方仓库很慢，还经常断线，所以要把仓库网址改成国内的镜像站。这里推荐使用官方镜像 registry.docker-cn.com 。下面是我的 Debian 系统的默认仓库修改方法，其他系统的修改方法参考<a href="https://www.docker-cn.com/registry-mirror">官方文档</a>。<br>
<br>打开 <code class="prettyprint">/etc/default/docker</code> 文件（需要 <code class="prettyprint">sudo</code> 权限），在文件的底部加上一行。<br>
<pre class="prettyprint">DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"<br>
</pre><br>
然后，重启 Docker 服务。<br>
<pre class="prettyprint">$ sudo service docker restart<br>
</pre><br>
现在就会自动从镜像仓库下载 image 文件了。<br>
<h3>方法 A：自建 WordPress 容器</h3>前面说过，本文会用三种方法演示 WordPress 的安装。第一种方法就是自建 WordPress 容器。<br>
<h4>官方的 PHP image</h4>首先，新建一个工作目录，并进入该目录。<br>
<pre class="prettyprint">$ mkdir docker-demo && cd docker-demo<br>
</pre><br>
然后，执行下面的命令。<br>
<pre class="prettyprint">$ docker container run \<br>
--rm \<br>
--name wordpress \<br>
--volume "$PWD/":/var/www/html \<br>
php:5.6-apache<br>
</pre><br>
上面的命令基于 <code class="prettyprint">php</code> 的 image 文件新建一个容器，并且运行该容器。<code class="prettyprint">php</code> 的标签是 <code class="prettyprint">5.6-apache</code>，说明装的是 PHP 5.6，并且自带 Apache 服务器。该命令的三个参数含义如下。<br>
<ul><li><code class="prettyprint">--rm</code>：停止运行后，自动删除容器文件。</li><li><code class="prettyprint">--name wordpress</code>：容器的名字叫做 <code class="prettyprint">wordpress</code>。</li><li><code class="prettyprint">--volume &quot;$PWD/&quot;:/var/www/html</code>：将当前目录（<code class="prettyprint">$PWD</code>）映射到容器的 <code class="prettyprint">/var/www/html</code>（Apache 对外访问的默认目录）。因此，当前目录的任何修改，都会反映到容器里面，进而被外部访问到。</li></ul><br>
<br>运行上面的命令以后，如果一切正常，命令行会提示容器对外的 IP 地址，请记下这个地址，我们要用它来访问容器。我分配到的 IP 地址是 172.17.0.2。<br>
<br>打开浏览器，访问 172.17.0.2，你会看到下面的提示。<br>
<pre class="prettyprint">Forbidden<br>
You don't have permission to access / on this server.<br>
</pre><br>
这是因为容器的 <code class="prettyprint">/var/www/html</code> 目录（也就是本机的 <code class="prettyprint">docker-demo</code> 目录）下面什么也没有，无法提供可以访问的内容。<br>
<br>请在本机的 <code class="prettyprint">docker-demo</code> 目录下面，添加一个最简单的 PHP 文件 <code class="prettyprint">index.php</code>。<br>
<pre class="prettyprint"><?php <br>
phpinfo();<br>
?><br>
</pre><br>
保存以后，浏览器刷新 <code class="prettyprint">172.17.0.2</code>，应该就会看到熟悉的 <code class="prettyprint">phpinfo</code> 页面了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/f40a0869edd3f3915af5d608741b8163.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/f40a0869edd3f3915af5d608741b8163.jpeg" class="img-polaroid" title="5.jpeg" alt="5.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>拷贝 WordPress 安装包</h4>既然本地的 <code class="prettyprint">docker-demo</code> 目录可以映射到容器里面，那么把 WordPress 安装包拷贝到 <code class="prettyprint">docker-demo</code> 目录下，不就可以通过容器访问到 WordPress 的安装界面了吗？<br>
<br>首先，在 <code class="prettyprint">docker-demo</code> 目录下，执行下面的命令，抓取并解压 WordPress 安装包。<br>
<pre class="prettyprint">$ wget https://cn.wordpress.org/wordpress-4.9.4-zh_CN.tar.gz<br>
$ tar -xvf wordpress-4.9.4-zh_CN.tar.gz<br>
</pre><br>
解压以后，WordPress 的安装文件会在 <code class="prettyprint">docker-demo/wordpress</code> 目录下。<br>
<br>这时浏览器访问 <code class="prettyprint">http://172.17.0.2/wordpress</code>，就能看到 WordPress 的安装提示了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/27136b401e7515ed681effe7d6688ea4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/27136b401e7515ed681effe7d6688ea4.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>官方的 MySQL 容器</h4>WordPress 必须有数据库才能安装，所以必须新建 MySQL 容器。<br>
<br>打开一个新的命令行窗口，执行下面的命令。<br>
<pre class="prettyprint">$ docker container run \<br>
-d \<br>
--rm \<br>
--name wordpressdb \<br>
--env MYSQL_ROOT_PASSWORD=123456 \<br>
--env MYSQL_DATABASE=wordpress \<br>
mysql:5.7<br>
</pre><br>
上面的命令会基于 MySQL 的 image 文件（5.7版本）新建一个容器。该命令的五个命令行参数的含义如下。<br>
<ul><li><code class="prettyprint">-d</code>：容器启动后，在后台运行。</li><li><code class="prettyprint">--rm</code>：容器终止运行后，自动删除容器文件。</li><li><code class="prettyprint">--name wordpressdb</code>：容器的名字叫做 <code class="prettyprint">wordpressdb</code></li><li><code class="prettyprint">--env MYSQL_ROOT_PASSWORD=123456</code>：向容器进程传入一个环境变量 <code class="prettyprint">MYSQL_ROOT_PASSWORD</code>，该变量会被用作 MySQL 的根密码。</li><li><code class="prettyprint">--env MYSQL_DATABASE=wordpress</code>：向容器进程传入一个环境变量 <code class="prettyprint">MYSQL_DATABASE</code>，容器里面的 MySQL 会根据该变量创建一个同名数据库（本例是 <code class="prettyprint">WordPress</code>）。</li></ul><br>
<br>运行上面的命令以后，正常情况下，命令行会显示一行字符串，这是容器的 ID，表示已经新建成功了。<br>
<br>这时，使用下面的命令查看正在运行的容器，你应该看到 <code class="prettyprint">wordpress</code> 和<code class="prettyprint">wordpressdb</code> 两个容器正在运行。<br>
<pre class="prettyprint">$ docker container ls<br>
</pre><br>
其中，<code class="prettyprint">wordpressdb</code> 是后台运行的，前台看不见它的输出，必须使用下面的命令查看。<br>
<pre class="prettyprint">$ docker container logs wordpressdb<br>
</pre><br>
<h4>定制 PHP 容器</h4>现在 WordPress 容器和 MySQL 容器都已经有了。接下来，要把 WordPress 容器连接到 MySQL 容器了。但是，PHP 的官方 image 不带有 <code class="prettyprint">mysql</code> 扩展，必须自己新建 image 文件。<br>
<br>首先，停掉 WordPress 容器。<br>
<pre class="prettyprint">$ docker container stop wordpress<br>
</pre><br>
停掉以后，由于 <code class="prettyprint">--rm</code> 参数的作用，该容器文件会被自动删除。<br>
<br>然后，在 <code class="prettyprint">docker-demo</code> 目录里面，新建一个 <code class="prettyprint">Dockerfile</code> 文件，写入下面的内容。<br>
<pre class="prettyprint">FROM php:5.6-apache<br>
RUN docker-php-ext-install mysqli<br>
CMD apache2-foreground<br>
</pre><br>
上面代码的意思，就是在原来 PHP 的 image 基础上，安装 <code class="prettyprint">mysqli</code> 的扩展。然后，启动 Apache。<br>
<br>基于这个 Dockerfile 文件，新建一个名为 <code class="prettyprint">phpwithmysql</code> 的 image 文件。<br>
<pre class="prettyprint">$ docker build -t phpwithmysql .<br>
</pre><br>
<h4>Wordpress 容器连接 MySQL</h4>现在基于 phpwithmysql image，重新新建一个 WordPress 容器。<br>
<pre class="prettyprint">$ docker container run \<br>
--rm \<br>
--name wordpress \<br>
--volume "$PWD/":/var/www/html \<br>
--link wordpressdb:mysql \<br>
phpwithmysql<br>
</pre><br>
跟上一次相比，上面的命令多了一个参数 <code class="prettyprint">--link wordpressdb:mysql</code>，表示 WordPress 容器要连到 <code class="prettyprint">wordpressdb</code> 容器，冒号表示该容器的别名是 <code class="prettyprint">mysql</code>。<br>
<br>这时还要改一下<code class="prettyprint">wordpress</code>目录的权限，让容器可以将配置信息写入这个目录（容器内部写入的<code class="prettyprint">/var/www/html</code>目录，会映射到这个目录）。<br>
<pre class="prettyprint">$ chmod -R 777 wordpress<br>
</pre><br>
接着，回到浏览器的 <code class="prettyprint">http://172.17.0.2/wordpress</code> 页面，点击“现在就开始！”按钮，开始安装。<br>
<br>WordPress 提示要输入数据库参数。输入的参数如下。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/d673ce4901b3660602c62e0b3521fd04.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/d673ce4901b3660602c62e0b3521fd04.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>数据库名：<code class="prettyprint">wordpress</code></li><li>用户名：<code class="prettyprint">root</code></li><li>密码：<code class="prettyprint">123456</code></li><li>数据库主机：<code class="prettyprint">mysql</code></li><li>表前缀：<code class="prettyprint">wp_</code>（不变）</li></ul><br>
<br>点击“下一步”按钮，如果 Wordpress 连接数据库成功，就会出现下面的页面，这就表示可以安装了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/8e8ec58cccad7013687fe4afd564c91a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/8e8ec58cccad7013687fe4afd564c91a.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
至此，自建 WordPress 容器的演示完毕，可以把正在运行的两个容器关闭了（容器文件会自动删除）。<br>
<pre class="prettyprint">$ docker container stop wordpress wordpressdb<br>
</pre><br>
<h3>方法 B：Wordpress 官方镜像</h3>上一部分的自建 WordPress 容器，还是挺麻烦的。其实不用这么麻烦，Docker 已经提供了官方 <a href="https://hub.docker.com/_/wordpress/">WordPress</a> image，直接用那个就可以了。有了上一部分的基础，下面的操作就很容易理解了。<br>
<h4>基本用法</h4>首先，新建并启动 MySQL 容器。<br>
<pre class="prettyprint">$ docker container run \<br>
-d \<br>
--rm \<br>
--name wordpressdb \<br>
--env MYSQL_ROOT_PASSWORD=123456 \<br>
--env MYSQL_DATABASE=wordpress \<br>
mysql:5.7<br>
</pre><br>
然后，基于官方的 WordPress image，新建并启动 WordPress 容器。<br>
<pre class="prettyprint">$ docker container run \<br>
-d \<br>
--rm \<br>
--name wordpress \<br>
--env WORDPRESS_DB_PASSWORD=123456 \<br>
--link wordpressdb:mysql \<br>
wordpress<br>
</pre><br>
上面命令中，各个参数的含义前面都解释过了，其中环境变量 <code class="prettyprint">WORDPRESS_DB_PASSWORD</code> 是 MySQL 容器的根密码。<br>
<br>上面命令指定 <code class="prettyprint">wordpress</code> 容器在后台运行，导致前台看不见输出，使用下面的命令查出 <code class="prettyprint">wordpress</code> 容器的 IP 地址。<br>
<pre class="prettyprint">$ docker container inspect wordpress<br>
</pre><br>
上面命令运行以后，会输出很多内容，找到 <code class="prettyprint">IPAddress</code> 字段即可。我的机器返回的 IP 地址是<code class="prettyprint">172.17.0.3</code>。<br>
<br>浏览器访问<code class="prettyprint">172.17.0.3</code>，就会看到 WordPress 的安装提示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/7d8a20dc6cc5fecdfff790c8b618588d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/7d8a20dc6cc5fecdfff790c8b618588d.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>WordPress 容器的定制</h4>到了上一步，官方 WordPress 容器的安装就已经成功了。但是，这种方法有两个很不方便的地方。<br>
<ul><li>每次新建容器，返回的 IP 地址不能保证相同，导致要更换 IP 地址访问 WordPress。</li><li>WordPress 安装在容器里面，本地无法修改文件。</li></ul><br>
<br>解决这两个问题很容易，只要新建容器的时候，加两个命令行参数就可以了。<br>
<br>先把刚才启动的 WordPress 容器终止（容器文件会自动删除）。<br>
<pre class="prettyprint">$ docker container stop wordpress<br>
</pre><br>
然后，使用下面的命令新建并启动 WordPress 容器。<br>
<pre class="prettyprint">$ docker container run \<br>
-d \<br>
-p 127.0.0.2:8080:80 \<br>
--rm \<br>
--name wordpress \<br>
--env WORDPRESS_DB_PASSWORD=123456 \<br>
--link wordpressdb:mysql \<br>
--volume "$PWD/wordpress":/var/www/html \<br>
wordpress<br>
</pre><br>
上面的命令跟前面相比，命令行参数只多出了两个。<br>
<ul><li><code class="prettyprint">-p 127.0.0.2:8080:80</code>：将容器的 80 端口映射到 <code class="prettyprint">127.0.0.2</code> 的 <code class="prettyprint">8080</code> 端口。</li><li><code class="prettyprint">--volume &quot;$PWD/wordpress&quot;:/var/www/html</code>：将容器的 <code class="prettyprint">/var/www/html</code> 目录映射到当前目录的 <code class="prettyprint">wordpress</code> 子目录。</li></ul><br>
<br>浏览器访问 <code class="prettyprint">127.0.0.2:8080:80</code> 就能看到 WordPress 的安装提示了。而且，你在 <code class="prettyprint">wordpress</code> 子目录下的每次修改，都会反映到容器里面。<br>
<br>最后，终止这两个容器（容器文件会自动删除）。<br>
<pre class="prettyprint">$ docker container stop wordpress wordpressdb<br>
</pre><br>
<h3>方法 C：Docker Compose 工具</h3>上面的方法 B 已经挺简单了，但是必须自己分别启动两个容器，启动的时候，还要在命令行提供容器之间的连接信息。因此，Docker 提供了一种更简单的方法，来管理多个容器的联动。<br>
<h4>Docker Compose 简介</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211013/91bd8bea8b73ed3f5e8b0a2999d024a2.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211013/91bd8bea8b73ed3f5e8b0a2999d024a2.jpeg" class="img-polaroid" title="10.jpeg" alt="10.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<a href="https://docs.docker.com/compose/">Compose</a> 是 Docker 公司推出的一个工具软件，可以管理多个 Docker 容器组成一个应用。你需要定义一个 <a href="https://www.ruanyifeng.com/blog/2016/07/yaml.html">YAML</a> 格式的配置文件 <code class="prettyprint">docker-compose.yml</code>，写好多个容器之间的调用关系。然后，只要一个命令，就能同时启动/关闭这些容器。<br>
<pre class="prettyprint"># 启动所有服务<br>
$ docker-compose up<br>
# 关闭所有服务<br>
$ docker-compose stop<br>
</pre><br>
<h4>Docker Compose 的安装</h4>Mac 和 Windows 在安装 Docker 的时候，会一起安装 docker compose。Linux 系统下的安装参考<a href="https://docs.docker.com/compose/install/#install-compose">官方文档</a>。<br>
<br>安装完成后，运行下面的命令。<br>
<pre class="prettyprint">$ docker-compose --version<br>
</pre><br>
<h4>WordPress 示例</h4>在 <code class="prettyprint">docker-demo</code> 目录下，新建 <code class="prettyprint">docker-compose.yml</code> 文件，写入下面的内容。<br>
<pre class="prettyprint">mysql:<br>
image: mysql:5.7<br>
environment:<br>
 - MYSQL_ROOT_PASSWORD=123456<br>
 - MYSQL_DATABASE=wordpress<br>
web:<br>
image: wordpress<br>
links:<br>
 - mysql<br>
environment:<br>
 - WORDPRESS_DB_PASSWORD=123456<br>
ports:<br>
 - "127.0.0.3:8080:80"<br>
working_dir: /var/www/html<br>
volumes:<br>
 - wordpress:/var/www/html<br>
</pre><br>
上面代码中，两个顶层标签表示有两个容器 <code class="prettyprint">mysql</code> 和 <code class="prettyprint">web</code>。每个容器的具体设置，前面都已经讲解过了，还是挺容易理解的。<br>
<br>启动两个容器。<br>
<pre class="prettyprint">$ docker-compose up<br>
</pre><br>
浏览器访问 <a href="http://127.0.0.3:8080/" rel="nofollow" target="_blank">http://127.0.0.3:8080</a>，应该就能看到 WordPress 的安装界面。<br>
<br>现在关闭两个容器。<br>
<pre class="prettyprint">$ docker-compose stop<br>
</pre><br>
关闭以后，这两个容器文件还是存在的，写在里面的数据不会丢失。下次启动的时候，还可以复用。下面的命令可以把这两个容器文件删除（容器必须已经停止运行）。<br>
<pre class="prettyprint">$ docker-compose rm<br>
</pre><br>
原文链接：<br>
<ul><li><a href="https://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html" rel="nofollow" target="_blank">https://www.ruanyifeng.com/blo ... .html</a></li><li><a href="https://www.ruanyifeng.com/blog/2018/02/docker-wordpress-tutorial.html" rel="nofollow" target="_blank">https://www.ruanyifeng.com/blo ... .html</a></li></ul>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            