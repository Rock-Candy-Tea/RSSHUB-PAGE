
---
title: '使用Cobra与Client-go实现Kubernetes自定义插件开发'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/cb7b3a1f8f8e9b9e1b69e70697231c3e.png'
author: Dockone
comments: false
date: 2021-07-21 13:14:09
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/cb7b3a1f8f8e9b9e1b69e70697231c3e.png'
---

<div>   
<br><h3>背景</h3>在我们使用kubectl查看Kubernetes资源的时候，想直接查看对应资源的容器名称和镜像名称，目前kubectl还不支持该选型，需要我们describe然后来查看，对于集群自己比较多，不是很方便，因此萌生了自己开发kubectl 插件来实现该功能。<br>
<h3>相关技术</h3><h4>Cobra</h4>Cobra是一个命令行程序库，是一个用来编写命令行的神器，提供了一个脚手架，用于快速生成基于Cobra应用程序框架。我们可以利用Cobra快速的去开发出我们想要的命令行工具，非常的方便快捷。<br>
<br>详细可参考：<a href="https://juejin.cn/post/6983299467537547294" rel="nofollow" target="_blank">https://juejin.cn/post/6983299467537547294</a><br>
<h4>Client-go</h4>在Kubernetes运维中，我们可以使用kubectl、客户端库或者REST请求来访问Kubernetes API。而实际上，无论是kubectl还是客户端库，都是封装了REST请求的工具。client-go作为一个客户端库，能够调用Kubernetes API，实现对Kubernetes集群中资源对象（包括Deployment、Service、Ingress、ReplicaSet、Pod、Namespace、Node等）的增删改查等操作。<br>
<br>详细可参考：<a href="https://juejin.cn/post/6962869412785487909" rel="nofollow" target="_blank">https://juejin.cn/post/6962869412785487909</a><br>
<h4>Kubernetes插件Krew</h4>Krew是类似于系统的apt、dnf或者brew的kubectl插件包管理工具，利用其可以轻松的完成kubectl插件的全面周期管理，包括搜索、下载、卸载等。<br>
<br>kubectl其工具已经比较完善，但是对于一些个性化的命令，其宗旨是希望开发者能以独立而紧张形式发布自定义的kubectl子命令，插件的开发语言不限，需要将最终的脚步或二进制可执行程序以<code class="prettyprint">kubectl-</code>的前缀命名，然后放到PATH中即可，可以使用<code class="prettyprint">kubectl plugin list</code>查看目前已经安装的插件。<br>
<br>详细可参考：<a href="https://juejin.cn/post/6969183421381738533" rel="nofollow" target="_blank">https://juejin.cn/post/6969183421381738533</a><br>
<h3>插件规划</h3><ul><li>插件命名为：kubeimg</li><li>目前仅简单实现一个image命令，用于查看不同资源对象（Deployments/DaemonSets/StatefulSets/Jobs/Cronjobs）的名称，和对应容器名称，镜像名称。</li><li>支持json格式输出。</li><li>最后将其作为krew插件使用。</li><li>可以直接根据名称空间来进行查看对应资源。</li></ul><br>
<br><h3>实战开发</h3><h4>项目初始化</h4>安装Cobra：<br>
<pre class="prettyprint">go get -v github.com/spf13/cobra/cobra<br>
</pre><br>
初始化项目：<br>
<pre class="prettyprint">$ ~/workspace/goworkspace/src/github.com/kaliarch/kubeimg  /Users/xuel/workspace/goworkspace/bin/cobra init --pkg-name kubeimg<br>
Your Cobra application is ready at<br>
/Users/xuel/workspace/goworkspace/src/github.com/kaliarch/kubeimg<br>
$ ~/workspace/goworkspace/src/github.com/kaliarch/kubeimg  ls<br>
LICENSE cmd     main.go<br>
$ ~/workspace/goworkspace/src/github.com/kaliarch/kubeimg  tree<br>
<br>
├── LICENSE<br>
├── cmd<br>
│   └── root.go<br>
└── main.go<br>
<br>
1 directory, 3 files<br>
</pre><br>
创建go mod，下载相关包：<br>
<pre class="prettyprint">go mod init kubeimg<br>
</pre><br>
<h4>增加子命令</h4>增加一个子命令image：<br>
<pre class="prettyprint">$ /Users/xuel/workspace/goworkspace/bin/cobra add image<br>
image created at /Users/xuel/workspace/goworkspace/src/github.com/kaliarch/kubeimg<br>
</pre><br>
<h4>添加参数</h4><pre class="prettyprint">// Execute adds all child commands to the root command and sets flags appropriately.<br>
// This is called by main.main(). It only needs to happen once to the rootCmd.<br>
func Execute() &#123;<br>
cobra.CheckErr(rootCmd.Execute())<br>
&#125;<br>
<br>
func init() &#123;<br>
KubernetesConfigFlags = genericclioptions.NewConfigFlags(true)<br>
imageCmd.Flags().BoolP("deployments", "d", false, "show deployments image")<br>
imageCmd.Flags().BoolP("daemonsets", "e", false, "show daemonsets image")<br>
imageCmd.Flags().BoolP("statefulsets", "f", false, "show statefulsets image")<br>
imageCmd.Flags().BoolP("jobs", "o", false, "show jobs image")<br>
imageCmd.Flags().BoolP("cronjobs", "b", false, "show cronjobs image")<br>
imageCmd.Flags().BoolP("json", "j", false, "show json format")<br>
KubernetesConfigFlags.AddFlags(rootCmd.PersistentFlags())<br>
&#125; <br>
</pre><br>
<h4>实现image命令</h4><pre class="prettyprint">var imageCmd = &cobra.Command&#123;<br>
Use:   "image",<br>
Short: "show resource image",<br>
Long:  `show k8s resource image`,<br>
RunE:  image,<br>
&#125;<br>
<br>
func init() &#123;<br>
rootCmd.AddCommand(imageCmd)<br>
&#125; <br>
</pre><br>
<h4>初始化Clientset</h4><pre class="prettyprint">// ClientSet k8s clientset<br>
func ClientSet(configFlags *genericclioptions.ConfigFlags) *kubernetes.Clientset &#123;<br>
config, err := configFlags.ToRESTConfig()<br>
if err != nil &#123;<br>
    panic("kube config load error")<br>
&#125;<br>
clientSet, err := kubernetes.NewForConfig(config)<br>
if err != nil &#123;<br>
<br>
    panic("gen kube config error")<br>
&#125;<br>
return clientSet<br>
&#125; <br>
</pre><br>
<h4>实现查看资源对象</h4>利用反射实现根据不同资源类型查看具体对应资源镜像及镜像名称功能。<br>
<pre class="prettyprint">func image(cmd *cobra.Command, args []string) error &#123;<br>
<br>
clientSet := kube.ClientSet(KubernetesConfigFlags)<br>
ns, _ := rootCmd.Flags().GetString("namespace")<br>
// 生命一个全局资源列表<br>
var rList []interface&#123;&#125;<br>
<br>
if flag, _ := cmd.Flags().GetBool("deployments"); flag &#123;<br>
    deployList, err := clientSet.AppsV1().Deployments(ns).List(context.Background(), v1.ListOptions&#123;&#125;)<br>
    if err != nil &#123;<br>
        fmt.Printf("list deployments error: %s", err.Error())<br>
    &#125;<br>
    rList = append(rList, deployList)<br>
&#125;<br>
...<br>
deployMapList := make([]map[string]string, 0)<br>
for i := 0; i < len(rList); i++ &#123;<br>
    switch t := rList[i].(type) &#123;<br>
    case *kv1.DeploymentList:<br>
        for k := 0; k < len(t.Items); k++ &#123;<br>
            for j := 0; j < len(t.Items[k].Spec.Template.Spec.Containers); j++ &#123;<br>
                deployMap := make(map[string]string)<br>
                deployMap["NAMESPACE"] = ns<br>
                deployMap["TYPE"] = "deployment"<br>
                deployMap["RESOURCE_NAME"] = t.Items[k].GetName()<br>
                deployMap["CONTAINER_NAME"] = t.Items[k].Spec.Template.Spec.Containers[j].Name<br>
                deployMap["IMAGE"] = t.Items[k].Spec.Template.Spec.Containers[j].Image<br>
                deployMapList = append(deployMapList, deployMap)<br>
            &#125;<br>
        &#125; <br>
</pre><br>
<h4>实现输出</h4>利用tabel来对结果进行输出：<br>
<pre class="prettyprint">func GenTable(mapList []map[string]string) *table.Table &#123;<br>
t, err := gotable.Create(title...)<br>
if err != nil &#123;<br>
    fmt.Printf("create table error: %s", err.Error())<br>
    return nil<br>
&#125;<br>
t.AddRows(mapList)<br>
return t<br>
&#125; <br>
</pre><br>
最终项目结构：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/cb7b3a1f8f8e9b9e1b69e70697231c3e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/cb7b3a1f8f8e9b9e1b69e70697231c3e.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>测试</h3>对完成的插件进行测试，编译<code class="prettyprint">go build</code>生成kubeimg二进制可执行文件。<br>
<h4>查看帮助</h4>查看所有帮助，其中可以看到cobra帮我们自动生成了help和completion两个命令，可以快速实现table补全，支持bash/fish/zsh/powershell：<br>
<pre class="prettyprint">./kubeimg --help<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/07fa2310f54f7ee757bb6a69601efe56.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/07fa2310f54f7ee757bb6a69601efe56.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/6a520763e2f07cbccdc172129a7a85c8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/6a520763e2f07cbccdc172129a7a85c8.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
查看image命令flags：<br>
<pre class="prettyprint">./kubeimg image --help<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/102bef076cc47d6128d91aab2428b895.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/102bef076cc47d6128d91aab2428b895.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>查看Deployment资源</h4>不知道ing名称名称空间，默认查看所有，名称空间下的资源：<br>
<pre class="prettyprint">./kubeimg image -d<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/a35e0a756982d7f0855d36eaa041d00d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/a35e0a756982d7f0855d36eaa041d00d.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>查看某个名称空间下资源</h4><pre class="prettyprint">./kubeimg image -d -n kube-system<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/6aa581cb433b6df19f88b35df873b0e1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/6aa581cb433b6df19f88b35df873b0e1.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>查看所有资源</h4>可以看到imlc-operator-controller-manager一个Pod中有两个container：<br>
<pre class="prettyprint">./kubeimg image -b -e -d -o -f<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/178e13132d689884c8279ea606d1bb6e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/178e13132d689884c8279ea606d1bb6e.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>json格式输出</h4><pre class="prettyprint">./kubeimg image -o -j<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/2470e6824a927851dcf869e00dd833c2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/2470e6824a927851dcf869e00dd833c2.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>作为krew插件使用</h3>需要将最终的脚步或二进制可执行程序以<code class="prettyprint">kubectl-</code>的前缀命名，然后放到PATH中即可，可以使用<code class="prettyprint">kubectl plugin list</code>查看目前已经安装的插件。<br>
<pre class="prettyprint">$ kubectl plugin list<br>
The following compatible plugins are available:=<br>
/usr/local/bin/kubectl-debug<br>
- warning: kubectl-debug overwrites existing command: "kubectl debug"<br>
/usr/local/bin/kubectl-v1.10.11<br>
/usr/local/bin/kubectl-v1.20.0<br>
/Users/xuel/.krew/bin/kubectl-df_pv<br>
/Users/xuel/.krew/bin/kubectl-krew<br>
<br>
# 将自己开发的插件重新命名为kubectl-img放到可执行路基下<br>
$ cp kubeimg /Users/xuel/.krew/bin/kubectl-img<br>
<br>
$ kubectl plugin list<br>
The following compatible plugins are available:=<br>
/usr/local/bin/kubectl-debug<br>
- warning: kubectl-debug overwrites existing command: "kubectl debug"<br>
/usr/local/bin/kubectl-v1.10.11<br>
/usr/local/bin/kubectl-v1.20.0<br>
/Users/xuel/.krew/bin/kubectl-df_pv<br>
/Users/xuel/.krew/bin/kubectl-krew<br>
/Users/xuel/.krew/bin/kubectl-img<br>
<br>
$ cp kubeimg /Users/xuel/.krew/bin/kubectl-img<br>
</pre><br>
之后就可以想使用kubectl插件一样使用了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210715/e9e0206eb9ab463a0d9bb96e01fdcd89.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210715/e9e0206eb9ab463a0d9bb96e01fdcd89.gif" class="img-polaroid" title="9-min.gif" alt="9-min.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>其他</h3>目前实现的比较简单，以此来抛砖引玉的功能，后期可以进行更多功能或其他插件的开发，自己动手丰衣足食。<br>
<br>后期待再完善开源到GitHub，个人主页：<a href="https://github.com/redhatxl" rel="nofollow" target="_blank">https://github.com/redhatxl</a>，以供大家学习交流。<br>
<br>原文链接：<a href="https://juejin.cn/post/6983324056502140964" rel="nofollow" target="_blank">https://juejin.cn/post/6983324056502140964</a>，作者：kaliarch
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            