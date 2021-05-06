
---
title: '写 Dockerfile 的一些技巧'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9369'
author: Dockone
comments: false
date: 2021-05-06 12:02:54
thumbnail: 'https://picsum.photos/400/300?random=9369'
---

<div>   
<br>和很多开源项目一样，SQLFlow 项目为了方便调试和协同工作，把所有 build tools 安装在一个 Docker image 里。项目的贡献者们用这个 Docker image 作为自己的开发环境。写 Dockerfile 的过程里，我们总结了一些技巧，分享如下，抛砖引玉。<br>
<h3>用 python -m pip 而不是 pip</h3>这是为了确保我们使用的 pip 是我们想用的那个 Python 对应的 pip。有时候，一个系统里安装了 Python 2 和 Python 3，而我们可能错误地设置了 PATH 环境变量（或则因为其他的原因），导致我们运行 Python 命令的时候，启动的 Python 3（或者 2），但是 pip 命令是 Python 2（或者3）的 pip。还有一些其他原因使我们更应该用 python -m pip 的，详见：<a href="https://link.zhihu.com/?target=https%3A//snarky.ca/why-you-should-use-python-m-pip/"></a><a href="https://snarky.ca/why-you-should-use-python-m-pip/" rel="nofollow" target="_blank">https://snarky.ca/why-you-should-use-python-m-pip/</a><br>
<br>一个典型的例子（升级 pip）。<br>
<pre class="prettyprint">python -m pip install --quiet --upgrade pip<br>
</pre><br>
<h3>让 pip install 更安静</h3>上例中，在 pip install 命令里，我们用了 --quiet 参数，减少 pip install 打印出来的信息。这样可以让 docker build 更安静。尤其是，如果在 CI 里运行 docker build 的话，减少打印信息可以让 CI log 更加可读。<br>
<h3>让 apt-get install 更安静</h3>类似的，用 apt-get 安装软件包的时候，我们用 -qq 命令，甚至重定向输出到 /dev/null 让它更安静。<br>
<pre class="prettyprint">apt-get -qq update<br>
apt-get -qq install -y curl > /dev/null<br>
</pre><br>
<h3>让 curl 和 wget 更安静</h3>首先，如果要下载文件，curl 和 wget 二选一即可。如果用 curl，可以用 --silent 参数。<br>
<pre class="prettyprint">curl -sLO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64<br>
</pre><br>
wget 有 --quiet 参数。<br>
<pre class="prettyprint">wget -q https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64<br>
</pre><br>
<h3>用 axel 而不是 curl 或者 wget</h3>作为一个开源软件，中外开发者都会运行 docker build。开发者所处的地理位置不同，各自都希望从距离自己最近（最快）的 mirror 下载和安装文件。axel 可以从多个 mirror 下载同一个文件，根据各个 mirror 的速度，决定分别从不同 mirror 下载的字节数量。如果有的 mirror 挂了，axel 可以忽略之。尤其对于身处国内的开发者，axel 完全可以取代 curl 以及 wget。<br>
<br>axel 和 wget 一样支持 --quiet 参数。以下是一个从大洋两岸的 mirrors 下载 Go 编译器的例子。<br>
<pre class="prettyprint">echo "Install Go compiler ..."<br>
GO_MIRROR_0="http://mirrors.ustc.edu.cn/golang/go1.13.4.linux-amd64.tar.gz"<br>
GO_MIRROR_1="https://dl.google.com/go/go1.13.4.linux-amd64.tar.gz"<br>
axel --quiet --output go.tar.gz $GO_MIRROR_0 $GO_MIRROR_1<br>
</pre><br>
<h3>让 Python <a href="http://setup.py/">setup.py</a> 更安静</h3>有时候我们会在 Dockerfile 里 build 和 install Python packages，此时我们需要运行：<br>
<pre class="prettyprint">python ./setup.py build --quiet<br>
python ./setup.py install --quiet<br>
</pre><br>
不过如果我们要 build binary distribution package，则需要注意使用全局参数 --quiet：<br>
<pre class="prettyprint">python ./setup.py --quiet bdist_wheel<br>
</pre><br>
<h3>明辨 ARG 和 ENV</h3>ARG 和 ENV 是 Dockerfile 里用来定制化 Docker image 的利器，经常结合在一起使用，也常领 Dockerfile 新手挠头。其实，记住一下几条规则，基本就可以了。<br>
<ol><li>ARG 存在于 docker build 命令执行期间。默认值写在 Dockerfile 里。如果需要修改，可以通过 docker build 命令里的 --build-arg 参数来指定。</li><li>ENV 存在于 docker run 命令执行期间。默认值写在 Dockerfile 里。如果要修改，可以通过 docker run 命令的 --env 参数来指定。</li><li>如果要把 ARG 的值保存到 container 运行起来之后仍然可以可用，则需要在 ARG 之后写一个 ENV。</li></ol><br>
<br>为了方便理解，请看下面几个例子。第一个例子：为了把 ARG 的值保存到 docker run 的时候也可以被用到，我们把它写入一个文件 /root/hello.sh。<br>
<pre class="prettyprint">FROM ubuntu:18.04<br>
ARG releaser=王益<br>
RUN echo "echo $releaser" > /root/hello.sh<br>
RUN chmod +x /root/hello.sh<br>
</pre><br>
这样，我们可以 docker run 的时候运行 /root/hello.sh，打印出 docker bulid 的时候指定的 releaser。<br>
<pre class="prettyprint">docker build -t dev .<br>
docker run --rm -it dev bash -c /root/hello.sh # 打印出 王益<br>
</pre><br>
不过因为 ARG 只存在于 docker build 命令执行期间，所以下面命令什么也打印不出来。<br>
<pre class="prettyprint">docker run --rm -it dev bash -c "echo $releaser"<br>
</pre><br>
如果要让上面命令也可以打印出 releaser 这个 ARG 的值，可以在 Dockerfile 里加一个 ENV。<br>
<pre class="prettyprint">FROM ubuntu:18.04<br>
ARG releaser=王益<br>
ENV releaser=$releaser<br>
</pre><br>
这样，下面命令就也可以打印出“王益”了。<br>
<pre class="prettyprint">docker build -t dev .<br>
docker run --rm -it dev bash -c "echo $releaser"<br>
</pre><br>
<h3>docker build --quiet</h3>上面一些经验是让 docker build 变得更安静的。如果要极端的安静，不需要通过在写 Dockerfile 的时候注意什么，只需要在 docker build 命令里加上 --quiet —— 如果不怕这样导致世界太过安静的话。<br>
<br>原文链接：<a href="https://zhuanlan.zhihu.com/p/147995194" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/147995194</a>，作者：王益
                                
                                                              
</div>
            