
---
title: '常用的几款工具让 Kubernetes 集群上的工作更容易'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210703/accf09cd1be082c801fa1952b37b06f4.gif'
author: Dockone
comments: false
date: 2021-07-07 14:07:17
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210703/accf09cd1be082c801fa1952b37b06f4.gif'
---

<div>   
<br>日常工作中在集群上的操作非常多，今天就来介绍我所使用的工具。<br>
<h3>kubectl-alias</h3>使用频率最高的工具，我自己稍微修改了一下，加入了 <code class="prettyprint">StatefulSet</code> 的支持。<br>
<br>这个是我的 <a href="https://github.com/addozhang/kubectl-aliases" rel="nofollow" target="_blank">https://github.com/addozhang/kubectl-aliases</a>，基于 <a href="https://github.com/ahmetb/kubectl-aliases" rel="nofollow" target="_blank">https://github.com/ahmetb/kubectl-aliases</a>。<br>
<br>比如输出某个 Pod 的 json，<code class="prettyprint">kgpoojson xxx</code> 等同于 <code class="prettyprint">kubectl get pod xxx -o json</code>。<br>
<br>结合 jq 使用效果更好。<br>
<br>语法解读：<br>
<ul><li><br><strong><code class="prettyprint">k</code></strong>=<code class="prettyprint">kubectl</code><br>
<ul><li><strong><code class="prettyprint">sys</code></strong>=<code class="prettyprint">--namespace kube-system</code></li></ul></li><li><br>commands：<br>
<ul><li><strong><code class="prettyprint">g</code></strong>=<code class="prettyprint">get</code></li><li><strong><code class="prettyprint">d</code></strong>=<code class="prettyprint">describe</code></li><li><strong><code class="prettyprint">rm</code></strong>=<code class="prettyprint">delete</code></li><li><strong><code class="prettyprint">a</code></strong>：<code class="prettyprint">apply -f</code></li><li><strong><code class="prettyprint">ak</code></strong>：<code class="prettyprint">apply -k</code></li><li><strong><code class="prettyprint">k</code></strong>：<code class="prettyprint">kustomize</code></li><li><strong><code class="prettyprint">ex</code></strong>：<code class="prettyprint">exec -i -t</code></li><li><strong><code class="prettyprint">lo</code></strong>：<code class="prettyprint">logs -f</code></li></ul></li></ul><br>
<br>resources：<br>
<ul><li><br><strong><code class="prettyprint">po</code></strong>=pod，<strong><code class="prettyprint">dep</code></strong>=<code class="prettyprint">deployment</code>，<strong><code class="prettyprint">ing</code></strong>=<code class="prettyprint">ingress</code>，<strong><code class="prettyprint">svc</code></strong>=<code class="prettyprint">service</code>，<strong><code class="prettyprint">cm</code></strong>=<code class="prettyprint">configmap</code>，<strong><code class="prettyprint">sec</code>=<code class="prettyprint">secret</code>*，</strong><code class="prettyprint">ns</code><strong>=<code class="prettyprint">namespace</code>，</strong><code class="prettyprint">no</code>**=<code class="prettyprint">node</code><br>
<ul><li>flags：</li></ul></li><li><br>output format：<strong><code class="prettyprint">oyaml</code></strong>，<strong><code class="prettyprint">ojson</code></strong>，<strong><code class="prettyprint">owide</code></strong></li><li><strong><code class="prettyprint">all</code></strong>：<code class="prettyprint">--all</code> or <code class="prettyprint">--all-namespaces</code> depending on the command</li><li><strong><code class="prettyprint">sl</code></strong>：<code class="prettyprint">--show-labels</code></li><li><br><strong><code class="prettyprint">w</code></strong>=<code class="prettyprint">-w/--watch</code><br>
<ul><li>value flags（should be at the end）：</li></ul></li><li><br>•<strong><code class="prettyprint">n</code></strong>=<code class="prettyprint">-n/--namespace</code></li><li><strong><code class="prettyprint">f</code></strong>=<code class="prettyprint">-f/--filename</code></li><li><strong><code class="prettyprint">l</code></strong>=<code class="prettyprint">-l/--selector</code></li></ul><br>
<br><h3>kubectx + kubens</h3>安装看这里：<br>
<br><code class="prettyprint">kubectx</code> 用于在不同的集群间进行快速切换。假如用 <code class="prettyprint">kubectl</code>，你需要：<br>
<pre class="prettyprint"># context 列表<br>
kubectl config current-context <br>
# 设置 context<br>
kubectl config use-context coffee<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210703/accf09cd1be082c801fa1952b37b06f4.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210703/accf09cd1be082c801fa1952b37b06f4.gif" class="img-polaroid" title="1.gif" alt="1.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>kubectx-demo</em><br>
<br><code class="prettyprint">kubens</code> 就是在不同 namespace 间快速切换的工具。用 <code class="prettyprint">kubectl</code> 的话，需要：<br>
<pre class="prettyprint"># namespace 列表<br>
kbuectl get ns<br>
# kubectl config set-context --current --namespace=kube-system<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210703/1c6b2673478d511ed9f4ea2480495df8.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210703/1c6b2673478d511ed9f4ea2480495df8.gif" class="img-polaroid" title="2.gif" alt="2.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
kubens-demo<br>
<h3>k9s</h3>没错，只比 k8s 多了个 1 。<br>
<br>k9s 提供了终端 UI 与 Kubernetes 集群进行编辑交互。本人常用的比如：<br>
<ul><li><code class="prettyprint">F</code> 配置端口转发</li><li><code class="prettyprint">l</code> 输出 Pod 日志</li><li><code class="prettyprint">e</code> 修改资源对象</li><li><code class="prettyprint">s</code> Pod 终端交互模式</li><li><code class="prettyprint">y</code> yaml 方式输出资源对象</li><li><code class="prettyprint">d</code> describe 资源对象</li><li><code class="prettyprint">ctrl+d</code> 删除 Pod</li></ul><br>
<br>启动方式：<br>
<pre class="prettyprint"># 指定 namespace 运行<br>
k9s -n mycoolns<br>
# 指定 context 运行<br>
k9s --context coolCtx<br>
# 只读模式运行<br>
k9s --readonly<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210703/eaf0c87395a8c9212b237493df88a67b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210703/eaf0c87395a8c9212b237493df88a67b.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>k9s-pod</em><br>
<br>键入问号“?” 就可以打开快捷操作指引。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210703/0865ab6e11b6e5eade2be78fef587a11.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210703/0865ab6e11b6e5eade2be78fef587a11.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>help</em><br>
<h3>stern</h3>stern 可以用来 <code class="prettyprint">tail</code> 集群上的多个 Pod 和 Pod 中多个容器的日志。不同的 Pod 和容器以不同的颜色区分，方便 debug。<br>
<br>比如使用命令 <code class="prettyprint">stern -l tier=control-plane -n kube-system</code> 可以输出 <code class="prettyprint">kube-system</code> 命名空间下控制平面（<code class="prettyprint">label</code> 为 <code class="prettyprint">tier=control-plane</code>） Pod 的日志。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210703/2a7db3afddfddd4b04526479c7a38842.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210703/2a7db3afddfddd4b04526479c7a38842.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>stern-control-plane</em><br>
<br>命令行选项：<br>
<pre class="prettyprint">Tail multiple pods and containers from Kubernetes<br>
Usage:<br>
stern pod-query [flags]<br>
Flags:<br>
-A, --all-namespaces             If present, tail across all namespaces. A specific namespace is ignored even if specified with --namespace.<br>
  --color string               Color output. Can be 'always', 'never', or 'auto' (default "auto")<br>
  --completion string          Outputs stern command-line completion code for the specified shell. Can be 'bash' or 'zsh'<br>
-c, --container string           Container name when multiple containers in pod (default ".*")<br>
  --container-state string     If present, tail containers with status in running, waiting or terminated. Default to running. (default "running")<br>
  --context string             Kubernetes context to use. Default to current context configured in kubeconfig.<br>
-e, --exclude strings            Regex of log lines to exclude<br>
-E, --exclude-container string   Exclude a Container name<br>
  --field-selector string      Selector (field query) to filter on. If present, default to ".*" for the pod-query.<br>
-h, --help                       help for stern<br>
-i, --include strings            Regex of log lines to include<br>
  --init-containers            Include or exclude init containers (default true)<br>
  --kubeconfig string          Path to kubeconfig file to use<br>
-n, --namespace strings          Kubernetes namespace to use. Default to namespace configured in Kubernetes context. To specify multiple namespaces, repeat this or set comma-separated value.<br>
-o, --output string              Specify predefined template. Currently support: [default, raw, json] (default "default")<br>
-l, --selector string            Selector (label query) to filter on. If present, default to ".*" for the pod-query.<br>
-s, --since duration             Return logs newer than a relative duration like 5s, 2m, or 3h. Defaults to 48h.<br>
  --tail int                   The number of lines from the end of the logs to show. Defaults to -1, showing all logs. (default -1)<br>
  --template string            Template to use for log lines, leave empty to use --output flag<br>
-t, --timestamps                 Print timestamps<br>
  --timezone string            Set timestamps to specific timezone (default "Local")<br>
-v, --version                    Print the version and exit<br>
</pre><br>
<h3>Lens</h3>Lens 是用来控制 Kubernetes 的 IDE，开源且免费。<br>
<br>消除了集群操作的复杂性、提供了实时的可观察性、方便故障排查、支持多系统的桌面客户端、兼容多种集群。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210703/476bb67ea2dc769249819b3d9c23701f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210703/476bb67ea2dc769249819b3d9c23701f.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Lens</em><br>
<h2>Infra App</h2>Infra App 跟 Lens 差不多，UI 较 Lens 好些，但是功能就弱很多，类似 Lens 的只读模式。<br>
<br>免费版比收费版的区别只在于支持的集群数量，免费版只支持一个集群。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210703/d28f0fc0d1749af061c405138f1bf12a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210703/d28f0fc0d1749af061c405138f1bf12a.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Infra</em><br>
<h3>kubefwd</h3>kubefwd，这个一直有安装但是使用次数寥寥，因为应用之间的访问没有走 service，不过偶尔做些实验的时候会用的上。<br>
<br><blockquote><br>kubefwd 是一个用于端口转发Kubernetes中指定namespace下的全部或者部分pod的命令行工具。kubefwd 使用本地的环回IP地址转发需要访问的service，并且使用与service相同的端口。kubefwd 会临时将service的域条目添加到 /etc/hosts 文件中。<br>
  <br>
  <br>启动kubefwd后，在本地就能像在Kubernetes集群中一样使用service名字与端口访问对应的应用程序。</blockquote><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210703/4ff73c5568b5bef8ee2467c5aeb3a386.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210703/4ff73c5568b5bef8ee2467c5aeb3a386.gif" class="img-polaroid" title="8.gif" alt="8.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>kubefwd_ani</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210703/795f463f63a3f9ccb7d0c18a73d4c185.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210703/795f463f63a3f9ccb7d0c18a73d4c185.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>善用工具可以提升效率，但并不是不可或缺的。<br>
<br>如果你有其他的工具，欢迎留言提出。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/uU2zmT5yyVcKZ5XmLSRqtg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/uU2zmT5yyVcKZ5XmLSRqtg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            