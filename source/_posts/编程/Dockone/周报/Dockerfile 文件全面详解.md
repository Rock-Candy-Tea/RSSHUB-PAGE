
---
title: 'Dockerfile 文件全面详解'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=1925'
author: Dockone
comments: false
date: 2021-08-24 10:08:33
thumbnail: 'https://picsum.photos/400/300?random=1925'
---

<div>   
<br>Docker 可以通过读取 Dockerfile 中的指令自动构建镜像。 Dockerfile 是一个文本文档，其中包含了用户创建镜像的所有命令和说明。<br>
<h4>一、 变量</h4>变量用 <strong>$variable_name</strong> 或者 <strong>$&#123;variable_name&#125;</strong> 表示。<br>
<ul><li><code class="prettyprint">$&#123;variable:-word&#125;</code> 表示如果 <code class="prettyprint">variable</code> 设置，则结果将是该值。如果 <code class="prettyprint">variable</code> 未设置，<code class="prettyprint">word</code> 则将是结果。</li><li><code class="prettyprint">$&#123;variable:+word&#125;</code> 表示如果 <code class="prettyprint">variable</code> 设置则为 <code class="prettyprint">word</code> 结果，否则为空字符串。</li></ul><br>
<br>变量前加 **** 可以转义成普通字符串：<code class="prettyprint">\$foo</code> or <code class="prettyprint">\$&#123;foo&#125;</code>，表示转换为 <code class="prettyprint">$foo</code> 和 <code class="prettyprint">$&#123;foo&#125;</code> 文字。<br>
<h4>二、FROM</h4>初始化一个新的构建阶段，并设置基础镜像：<br>
<pre class="prettyprint">FROM [--platform=<platform>] <image> [AS <name>]<br>
FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]<br>
FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]<br>
</pre><br>
<ul><li>单个 Dockfile 可以多次出现 <strong>FROM</strong>，以使用之前的构建阶段作为另一个构建阶段的依赖项</li><li><code class="prettyprint">AS name</code> 表示为构建阶段命名，在后续 <code class="prettyprint">FROM</code> 和 <code class="prettyprint">COPY --from=&lt;name></code> 说明中可以使用这个名词，引用此阶段构建的映像</li><li><code class="prettyprint">digest</code> 其实就是就是根据镜像内容产生的一个 ID，只要镜像的内容不变 digest 也不会变</li><li><code class="prettyprint">tag</code> 或 <code class="prettyprint">digest</code> 值是可选的。如果您省略其中任何一个，构建器默认使用一个 <code class="prettyprint">latest</code> 标签。如果找不到该 <code class="prettyprint">tag</code> 值，构建器将返回错误。</li><li><code class="prettyprint">--platform</code> 标志可用于在 <code class="prettyprint">FROM</code> 引用多平台镜像的情况下指定平台。例如，<code class="prettyprint">linux/amd64</code>、<code class="prettyprint">linux/arm64</code>、 或 <code class="prettyprint">windows/amd64</code>。</li></ul><br>
<br><h4>三、RUN</h4>将在当前镜像之上的新层中执行命令，在 docker build时运行。<br>
<pre class="prettyprint">RUN /bin/bash -c 'source $HOME/.bashrc; \<br>
echo $HOME'<br>
</pre><br>
RUN 有两种形式：<br>
<ul><li><code class="prettyprint">RUN &lt;command></code>（shell 形式，命令在 shell 中运行，默认 <code class="prettyprint">/bin/sh -c</code> 在 Linux 或 <code class="prettyprint">cmd /S /C</code>Windows 上）</li><li><code class="prettyprint">RUN [&quot;executable&quot;, &quot;param1&quot;, &quot;param2&quot;]</code>（执行形式）</li></ul><br>
<br>说明：<br>
<ul><li>可以使用 <code class="prettyprint">\</code>（反斜杠）将单个 RUN 指令延续到下一行</li><li><code class="prettyprint">RUN</code> 在下一次构建期间，指令缓存不会自动失效。可以使用 <code class="prettyprint">--no-cache</code> 标志使指令缓存无效</li><li>Dockerfile 的指令每执行一次都会在 Docker 上新建一层。所以过多无意义的层，会造成镜像膨胀过大，可以使用 <strong>&&</strong> 符号连接命令，这样执行后，只会创建 1 层镜像</li></ul><br>
<br><h4>四、CMD</h4>运行程序，在 docker run 时运行，但是和 run 命令不同，RUN 是在 docker build 时运行。<br>
<pre class="prettyprint">FROM ubuntu<br>
CMD ["/usr/bin/wc","--help"]<br>
</pre><br>
支持三种格式：<br>
<ul><li><code class="prettyprint">CMD [&quot;executable&quot;,&quot;param1&quot;,&quot;param2&quot;]</code> 使用 <code class="prettyprint">exec</code> 执行，推荐方式；</li><li><code class="prettyprint">CMD command param1 param2</code> 在 <code class="prettyprint">/bin/sh</code> 中执行，提供给需要交互的应用；</li><li><code class="prettyprint">CMD [&quot;param1&quot;,&quot;param2&quot;]</code> 提供给 <code class="prettyprint">ENTRYPOINT</code> 的默认参数。</li></ul><br>
<br>指定启动容器时执行的命令，每个 Dockerfile 只能有一条 <code class="prettyprint">CMD</code> 命令。如果指定了多条命令，只有最后一条会被执行。<br>
<br>如果用户启动容器时候指定了运行的命令，则会覆盖掉 <code class="prettyprint">CMD</code> 指定的命令。<br>
<h4>五、LABEL</h4>添加元数据：<br>
<pre class="prettyprint">LABEL multi.label1="value1" \<br>
  multi.label2="value2" \<br>
  other="value3"<br>
</pre><br>
<h4>六、EXPOSE</h4><pre class="prettyprint">EXPOSE <port> [<port>/<protocol>...]<br>
</pre><br>
Docker 容器在运行时侦听指定的网络端口。可以指定端口是监听TCP还是UDP，如果不指定协议，默认为TCP。<br>
<br>该 <code class="prettyprint">EXPOSE</code> 指令实际上并未发布端口。要在运行容器时实际发布端口，<code class="prettyprint">docker run</code>  -P 来发布和映射一个或多个端口。<br>
<br>默认情况下，<code class="prettyprint">EXPOSE</code> 假定 TCP。您还可以指定 UDP：<br>
<pre class="prettyprint">EXPOSE 80/udp<br>
</pre><br>
<h4>七、ENV</h4>设置环境变量：<br>
<pre class="prettyprint">ENV <key>=<value> ...<br>
</pre><br>
设置的环境变量将持续存在，您可以使用 <code class="prettyprint">docker inspect</code> 来查看。使用 <code class="prettyprint">docker run --env &lt;key>=&lt;value></code> 来更改环境变量的值。<br>
<br>如果环境变量只在构建期间需要，请考虑为单个命令设置一个值：<br>
<pre class="prettyprint">RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y ...<br>
</pre><br>
或者使用 <code class="prettyprint">ARG</code>，它不会保留在最终镜像中：<br>
<pre class="prettyprint">ARG DEBIAN_FRONTEND=noninteractive<br>
RUN apt-get update && apt-get install -y ...<br>
</pre><br>
<h4>八、ADD</h4>复制新文件、目录或远程文件 URL <code class="prettyprint">&lt;src></code>  ，并将它们添加到 <code class="prettyprint">&lt;dest></code> 中。<br>
<br><code class="prettyprint">&lt;src></code> 可以指定多个资源，但如果它们是文件或目录，则它们的路径被解释为相对于构建上下文的源，也就是 <strong>WORKDIR</strong>。<br>
<br>每个都 <code class="prettyprint">&lt;src></code> 可能包含通配符，匹配将使用 Go 的 filepath.Match 规则。例如：<br>
<br>添加所有以“hom”开头的文件：<br>
<pre class="prettyprint">ADD hom* /mydir/<br>
</pre><br>
在下面的示例中，<code class="prettyprint">?</code> 被替换为任何单个字符，例如“home.txt”。<br>
<pre class="prettyprint">ADD hom?.txt /mydir/<br>
</pre><br>
<code class="prettyprint">&lt;dest></code> 是一个绝对路径，或相对 <code class="prettyprint">WORKDIR</code> 的相对路径。<br>
<h4>九、COPY</h4>语法同ADD一致，复制拷贝文件。<br>
<br>COPY 指令和 ADD 指令的唯一区别在于：是否支持从远程URL获取资源。COPY 指令只能从执行 docker build 所在的主机上读取资源并复制到镜像中。而 ADD 指令还支持通过 URL 从远程服务器读取资源并复制到镜像中。<br>
<br>相同需求时，推荐使用 COPY 指令。ADD 指令更擅长读取本地tar文件并解压缩。<br>
<h4>十、ENTRYPOINT</h4><strong>ENTRYPOINT</strong> 和 <strong>CMD</strong> 一样，都是在指定容器启动程序及参数，不过它不会被 docker run 的命令行参数指定的指令所覆盖。如果要覆盖的话，需要通过 docker run --entrypoint 来指定。<br>
<br>它有2种格式：<br>
<pre class="prettyprint">ENTRYPOINT ["executable", "param1", "param2"]<br>
ENTRYPOINT command param1 param2<br>
</pre><br>
当指定了 ENTRYPOINT 后， CMD 的内容作为参数传给 ENTRYPOINT 指令，实际执行时，将变为：<br>
<pre class="prettyprint"><ENTRYPOINT> <CMD><br>
</pre><br>
<h4>十一、VOLUME</h4>创建一个具有指定名称的挂载数据卷。<br>
<pre class="prettyprint">VOLUME ["/var/log/"]<br>
VOLUME /var/log<br>
</pre><br>
<br>它的主要作用是：<br>
<ul><li>避免重要的数据，因容器重启而丢失</li><li>避免容器不断变大</li></ul><br>
<br><h4>十二、ARG</h4>定义变量，与 <strong>ENV</strong> 作用相同，不过 <code class="prettyprint">ARG</code> 变量不会像 <code class="prettyprint">ENV</code> 变量那样持久化到构建好的镜像中。<br>
<pre class="prettyprint">ARG <name>[=<default value>]<br>
</pre><br>
Docker 有一组预定义的 <code class="prettyprint">ARG</code> 变量，您可以在 Dockerfile 中没有相应指令的情况下使用这些变量。<br>
<ul><li><code class="prettyprint">HTTP_PROXY</code></li><li><code class="prettyprint">http_proxy</code></li><li><code class="prettyprint">HTTPS_PROXY</code></li><li><code class="prettyprint">https_proxy</code></li><li><code class="prettyprint">FTP_PROXY</code></li><li><code class="prettyprint">ftp_proxy</code></li><li><code class="prettyprint">NO_PROXY</code></li><li><code class="prettyprint">no_proxy</code></li></ul><br>
<br>要使用这些，请使用 <code class="prettyprint">--build-arg</code> 标志在命令行上传递它们，例如：<br>
<pre class="prettyprint">docker build --build-arg HTTPS_PROXY=https://my-proxy.example.com .<br>
</pre><br>
<h4>十三、ONBUILD</h4>将一个触发指令添加到镜像中，以便稍后在该镜像用作另一个构建的基础时执行。也就是另外一个 dockerfile FROM 了这个镜像的时候执行。<br>
<pre class="prettyprint">ONBUILD ADD . /app/src<br>
ONBUILD RUN /usr/local/bin/python-build --dir /app/src<br>
</pre><br>
<h4>十四、STOPSIGNAL</h4>设置将发送到容器退出的系统调用信号。该信号可以是与内核系统调用表中的位置匹配的有效无符号数，例如 9，或格式为 SIGNAME 的信号名称，例如 SIGKILL。<br>
<pre class="prettyprint">STOPSIGNAL signal<br>
</pre><br>
默认的 stop-signal 是 <strong>SIGTERM</strong>，在 docker stop 的时候会给容器内 PID 为 1 的进程发送这个 signal，通过 --stop-signal 可以设置自己需要的 signal，主要目的是为了让容器内的应用程序在接收到 signal 之后可以先处理一些事物，实现容器的平滑退出，如果不做任何处理，容器将在一段时间之后强制退出，会造成业务的强制中断，默认时间是 10s。<br>
<h4>十五、HEALTHCHECK</h4>用于指定某个程序或者指令来监控 Docker 容器服务的运行状态。该 <code class="prettyprint">HEALTHCHECK</code> 指令有两种形式：<br>
<ul><li><code class="prettyprint">HEALTHCHECK [OPTIONS] CMD command</code>（通过在容器内运行命令来检查容器健康状况）</li><li><code class="prettyprint">HEALTHCHECK NONE</code>（禁用从基础镜像继承的任何健康检查）</li></ul><br>
<br><h4>十六、SHELL</h4>覆盖用于命令的 <strong>shell</strong> 形式的默认 shell。Linux 上的默认 shell 是 <code class="prettyprint">[&quot;/bin/sh&quot;, &quot;-c&quot;]</code>，Windows 上是 <code class="prettyprint">[&quot;cmd&quot;, &quot;/S&quot;, &quot;/C&quot;]</code>。<br>
<pre class="prettyprint">SHELL ["executable", "parameters"]<br>
</pre><br>
该 <code class="prettyprint">SHELL</code> 指令在 Windows 上特别有用，因为 Windows 有两种常用且截然不同的本机 SHELL：<code class="prettyprint">cmd</code> 和 <code class="prettyprint">powershell</code>，以及可用的备用 shell，包括 <code class="prettyprint">sh</code>。该 SHELL 指令可以出现多次。每条 SHELL 指令都会覆盖所有先前的 SHELL 指令，并影响所有后续指令。<br>
<h4>十七、WORKDIR</h4>工作目录，如果 <code class="prettyprint">WORKDIR</code> 不存在，即使它没有在后续 <code class="prettyprint">Dockerfile</code> 指令中使用，它也会被创建。<br>
<br>docker build 构建镜像过程中，每一个 RUN 命令都会新建一层。只有通过 WORKDIR 创建的目录才会一直存在。<br>
<br>可以设置多个 WORKDIR，如果提供了相对路径，它将相对于前一条 <code class="prettyprint">WORKDIR</code> 指令的路径。例如：<br>
<pre class="prettyprint">WORKDIR /a<br>
WORKDIR b<br>
WORKDIR c<br>
RUN pwd<br>
</pre><br>
最终 <code class="prettyprint">pwd</code> 命令的输出是 <code class="prettyprint">/a/b/c</code>。<br>
<br>该 <code class="prettyprint">WORKDIR</code> 指令可以解析先前使用 <code class="prettyprint">ENV</code>，例如：<br>
<pre class="prettyprint">ENV DIRPATH=/path<br>
WORKDIR $DIRPATH/$DIRNAME<br>
RUN pwd<br>
</pre><br>
最终 <code class="prettyprint">pwd</code> 命令的输出是 <code class="prettyprint">/path/$DIRNAME</code>。<br>
<h4>十八、USER</h4>设置用户名（或 UID）和可选的用户组（或 GID）。<br>
<pre class="prettyprint">USER <user>[:<group>]<br>
USER <UID>[:<GID>]<br>
</pre><br>
原文链接：<a href="https://zhuanlan.zhihu.com/p/387855002" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/387855002</a>
                                
                                                              
</div>
            