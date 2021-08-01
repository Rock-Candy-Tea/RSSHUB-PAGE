
---
title: 'Google Breakpad 源码解析（一）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c19167a8331a42d89a79bbf9d089db7e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 00:24:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c19167a8331a42d89a79bbf9d089db7e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">系列文章</h2>
<ul>
<li><a href="https://juejin.cn/post/6991374121388998687" target="_blank" title="https://juejin.cn/post/6991374121388998687">Google Breakpad 源码解析（一）</a></li>
</ul>
<h2 data-id="heading-1">简介</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fchromium.googlesource.com%2Fbreakpad%2Fbreakpad" target="_blank" rel="nofollow noopener noreferrer" title="https://chromium.googlesource.com/breakpad/breakpad" ref="nofollow noopener noreferrer">Breakpad</a> 是 Google 开源的，用于实现崩溃上报（crash-report）的系统，其中包括客户端和服务端两部分。</p>
<blockquote>
<p>官网上的介绍：</p>
<p>Breakpad is a set of client and server components which implement a crash-reporting system.</p>
</blockquote>
<h2 data-id="heading-2">编译构建</h2>
<p>Breakpad 的源码依赖管理使用的是 Google 自己开发的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcommondatastorage.googleapis.com%2Fchrome-infra-docs%2Fflat%2Fdepot_tools%2Fdocs%2Fhtml%2Fdepot_tools_tutorial.html%23_setting_up" target="_blank" rel="nofollow noopener noreferrer" title="https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html#_setting_up" ref="nofollow noopener noreferrer">depot_tools</a>，但因为某些特殊原因，使用 depot_tools 下载源码经常会卡住，所以网上也有很多教程是让大家直接用 git 下载，相关文章很多这里就不贴链接了。</p>
<p>Breakpad 构建出来的脚本是区分系统环境的，所以要根据当前使用系统，构建不同的产物。Breakpad 目前支持 macOS、Linux 和 Windows 三个系统环境的构建。</p>
<p>笔者自己本身是 macOS(Mojave 10.14.4) 环境，但是没有编译成功，提示缺少某些依赖库，最后索性用 Docker 跑了个 Linux(ubuntu 18.04) 镜像，意外的顺利，一次成功了。</p>
<p>这里放上 Dockerfile 和 docker-compose.yml，习惯使用 docker-compose 了。</p>
<p>Dockerfile</p>
<pre><code class="copyable"> FROM ubuntu:18.04
 ​
 # 配置 git
 ENV DEBIAN_FRONTEND=noninteractive
 RUN apt update && \
     apt install --no-install-recommends git-all curl wget build-essential --assume-yes
 ​
 # 配置 depot_tools
 RUN cd /opt && \
     git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
 ENV PATH $&#123;PATH&#125;:/opt/depot_tools
 ​
 COPY src/ /opt/breakpad/
 ​
 # 配置 breakpad
 RUN cd /opt/breakpad && \
     ./configure && \
     make && \
     make install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里之所以使用 <code>COPY</code> 命令拷贝 breakpad 源码，是因为需要修改 Breakpad 源码，这样可以方便调试。</p>
<p>docker-compose.yml</p>
<pre><code class="copyable"> version: "3.7"
 ​
 services:
     yybreakpad:
         build: ./
         command: tail -F anything
         volumes:
             - ./temp:/opt/temp
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这条命令是让 docker 容器不自动退出：</p>
<pre><code class="copyable"> command: tail -F anything
<span class="copy-code-btn">复制代码</span></code></pre>
<p>挂载了 temp 目录，可以将一些执行完的产物放到这个目录里面，不需要频繁在容器和主机之间拷贝：</p>
<pre><code class="copyable"> volumes:
     - ./temp:/opt/temp
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是构建目录的层级结构：</p>
<pre><code class="copyable"> ├── Dockerfile
 ├── docker-compose.yml
 ├── src
 └── temp
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">架构</h2>
<p>先放一张 Breakpad 官方的架构图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c19167a8331a42d89a79bbf9d089db7e~tplv-k3u1fbpfcp-zoom-1.image" alt="Breakpad-System" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Breakpad 主要由三个部分组成：</p>
<ul>
<li>Client，当端上发生崩溃时，会默认生成 minidump 文件。</li>
<li>Symbol Dumper，这个工具用于生成 Breakpad 专属的符号表，要作用在带有调试信息原始库才行。</li>
<li>Processor，这个工具通过读取 Client 生成的 minidump 文件，再去匹配 Symbol Dumper 生成的对应符号表，最后生成人类可读的 C/C++ 堆栈跟踪。</li>
</ul>
<h3 data-id="heading-4">minidump 格式</h3>
<p>minidump 文件可以认为是 coredump 文件的简化版，之所以使用它，官方的理由是：</p>
<ul>
<li>coredump 非常大，在端上传输不方便。</li>
<li>coredump 记录不全，例如，Linux 标准库没有描述寄存器如何存储在 PT_NOTE 段中。</li>
<li>说服 Windows 机器生成 coredump 比 其他系统生成 minidump 更难。</li>
<li>实现各平台的 dump 文件格式统一。</li>
</ul>
<h3 data-id="heading-5">处理流程（以 Linux 为例）</h3>
<ol>
<li>
<p>dump_syms</p>
<p>当我们用 C/C++ 代码编写了一个库后，编译器默认会生成带调试信息的 ELF 文件，这时候我们可以通过执行以下命令生成符号表：</p>
<pre><code class="copyable"> dump_syms [elf_file] > [elf_file.sym]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>elf_file.sym 不是强制格式，可以使用任意文件名称和后缀。</p>
<blockquote>
<p>带调试信息的 ELF 文件要大的多，所以，一般端上使用的是 strip 后的文件，这会剔除一些不必要的信息，让文件变得更小。</p>
</blockquote>
<p><strong>生成的符号表需要按照指定格式存放，这里后面才能正确匹配上</strong>，首先是外层的目录名字需要是 ELF 文件的名称，包含后缀，接着是符号表 ID 的目录，最后才是存放对应符号表。</p>
<p>例如：</p>
<pre><code class="copyable"> └── symbols
     └── libtest.so
         └── D6CAF1C3E374EFD057659926ABA14AD00
             └── libtest.so.sym
<span class="copy-code-btn">复制代码</span></code></pre>
<p>符号 ID 可以通过读取符号表文件的首行获取：</p>
<pre><code class="copyable"> $ head -n1 libtest.so.sym
 MODULE Linux arm D6CAF1C3E374EFD057659926ABA14AD00 libtest.so
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 D6CAF1C3E374EFD057659926ABA14AD00 就是对应符号表的 ID。</p>
</li>
<li>
<p>minidump_writer</p>
<p>Breakpad Client 组件提前注册好 SIGSEGV、SIGABRT 等异常信号的回调方法，当端上发生崩溃时，会生成 minidump 文件，其中会包含<strong>线程信息</strong>、<strong>链接库信息</strong>、<strong>堆栈信息</strong> 等等。</p>
</li>
<li>
<p>symupload（可选）</p>
<p>Breakpad 支持将生成的 minidump 文件上传到指定服务器，这是可选的步骤，可以选择自己上传。</p>
</li>
<li>
<p>minidump_stackwalk</p>
<p>在获取到 minidump 文件后，就可以使用 minidump_stackwalk 配合对应的符号表，将 minidump 文件解析成人类可读的堆栈跟踪了。</p>
<pre><code class="copyable"> minidump_stackwalk [minidump_file] ./symbols > [stacktrace_file]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>./symbols</code> 是用于指定符号表目录，具体内容可以看步骤 1，<code>[stacktrace_file]</code> 用于保存最终生成的堆栈跟踪。</p>
</li>
</ol>
<h3 data-id="heading-6">符号表匹配（以 Linux 为例）</h3>
<p>minidump 文件是<strong>根据符号 ID 来匹配对应的符号表</strong>。</p>
<p>符号 ID 的生成规则，<strong>默认会使用 ELF 文件中的 BuildId，如果不存在 BuildId，则会根据 text section 摘要生成</strong>。对应代码片段如下：</p>
<blockquote>
<p>text section 在 ELF 文件中一般用来存放代码部分，所以这里可以理解为根据代码做摘要。</p>
<p>关于 ELF 文件格式，可以通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FExecutable_and_Linkable_Format" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format" ref="nofollow noopener noreferrer">wiki</a> 来做更深入了解。</p>
</blockquote>
<pre><code class="copyable"> // https://chromium.googlesource.com/breakpad/breakpad/+/refs/heads/main/src/common/linux/file_id.cc
 // static
 bool FileID::ElfFileIdentifierFromMappedFile(const void* base,
                                              wasteful_vector<uint8_t>& identifier) &#123;
   // Look for a build id note first.
   // 首先使用 build id
   if (FindElfBuildIDNote(base, identifier))
     return true;
   // Fall back on hashing the first page of the text section.
   // 否则，使用 text section 的 hash 值
   return HashElfTextSection(base, identifier);
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，<strong>当我们使用 minidump_stackwalk 没有把符号地址转换成对应的符号时，可以检查下符号 ID 是否匹配正确</strong>。</p>
<h2 data-id="heading-7">小结</h2>
<p>Breakpad 总体架构是非常清晰的，每个模块负责的职责都不一样，<strong>Client 在端上捕获 crash 并生成 minidump 上报，服务端利用提前生成的符号表，使用 minidump_stackwalk 将 minidump 解析成人类可读的堆栈跟踪</strong>。</p>
<p>这一节，我们主要是从宏观上去看 Breakpad 的总体设计，包括编译构建，使用流程等等，这有助我们在下一节，对 Breakpad 的源码解析。</p></div>  
</div>
            