
---
title: '如何使用Go调用Kubernetes API-类型和普通机制'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220417/a3a2c8c176535479563ed7fc6d92bf5e.png'
author: Dockone
comments: false
date: 2022-05-14 00:52:03
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220417/a3a2c8c176535479563ed7fc6d92bf5e.png'
---

<div>   
<br>【编者的话】本文带你打开Kubernetes API的探索之旅的正确姿势，快来一睹为快吧！<br>
<br>官方的Kubernetes Go客户端装载了高级抽象——<code class="prettyprint">Clientset</code>、<code class="prettyprint">Informers</code>、<code class="prettyprint">Cache</code>、<code class="prettyprint">Scheme</code>、<code class="prettyprint">Discovery</code>，哦，天哪！当我尝试在没有学习移动部分的情况下使用它时，我遇到了大量的新概念。这是一次不愉快的经历，但更重要的是，它削弱了我在代码中做出明智决定的能力。<br>
<br>因此，我决定通过对客户端组件的彻底研究来解开这个谜。<br>
<br>但是从哪里开始呢？在剖析<code class="prettyprint">client-go</code>本身之前，了解它的两个主要依赖项可能是一个好主意，<code class="prettyprint">k8s.io/api</code>和<code class="prettyprint">k8s.io/apimachinery</code>模块。这将简化主要任务，但这不是唯一的好处。这两个模块被分离出来是有原因的——它们不仅可以被客户端使用，也可以被服务器端使用，或者被处理Kubernetes对象的任何其他软件使用。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220417/a3a2c8c176535479563ed7fc6d92bf5e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220417/a3a2c8c176535479563ed7fc6d92bf5e.png" class="img-polaroid" title="01.png" alt="01.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>API资源、类和对象</h3>首先，快速<a href="http://dockone.io/article/2434811">回顾一下</a>。熟悉以下概念对进一步讨论的成功至关重要：<br>
<ul><li>资源类型——一个由Kubernetes API端点服务的实体：Pod、Deployment、ConfigMap等。</li><li>API组——资源类型被组织成版本化的逻辑组：apps/v1、batch/v1、storage.k8s.io/v1beta1等等。</li><li>对象——一个资源实例——每个API端点都处理特定资源类型的对象。</li><li>类——API返回或接受的每个对象都必须符合一个对象模式——由其类型定义的属性的特定组合Pod、Deployment、ConfigMap等。</li></ul><br>
<br>同样重要的是要区分广义对象和Kubernetes的“一级”对象——像Pod、Service或Secret这样的持久实体，它们作为集群的意图的记录。虽然为了序列化和反序列化，每个API对象都必须有一个API版本和类型属性，但并不是每个API对象都是“一级”Kubernetes对象。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220417/2701cac14b48c42646f1171fe8a1ce9c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220417/2701cac14b48c42646f1171fe8a1ce9c.png" class="img-polaroid" title="02.png" alt="02.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>k8s.io/api模块</h3>Go是一种静态类型的编程语言。那么，与Pod、ConfigMap、Secret和其他一级Kubernetes对象对应的所有结构在哪里呢？对，在k8s.io/api。<br>
<br>尽管命名松散，k8.io/api模块似乎只用于API类型定义。它充满了固定结构，与我们都知道和喜爱的YAML体现的那些内容非常相似：<br>
<pre class="prettyprint">package main<br>
<br>
import (<br>
"fmt"<br>
<br>
appsv1 "k8s.io/api/apps/v1"<br>
corev1 "k8s.io/api/core/v1"<br>
)<br>
<br>
func main() &#123;<br>
deployment := appsv1.Deployment&#123;<br>
Spec: appsv1.DeploymentSpec&#123;<br>
  Template: corev1.PodTemplateSpec&#123;<br>
    Spec: corev1.PodSpec&#123;<br>
      Containers: []corev1.Container&#123;<br>
        &#123; Name:  "web", Image: "nginx:1.21" &#125;,<br>
      &#125;,<br>
    &#125;,<br>
  &#125;,<br>
&#125;,<br>
&#125;<br>
<br>
fmt.Printf("%#v", &deployment)<br>
&#125; <br>
</pre><br>
这个模块不仅定义了顶层的Kubernetes对象，就像上面的部署一样，还为它们的内部属性定义了许多辅助类型：<br>
<pre class="prettyprint">// PodSpec is a description of a pod.<br>
type PodSpec struct &#123;<br>
Volumes []Volume `json:"volumes,omitempty" patchStrategy:"merge,retainKeys" patchMergeKey:"name" protobuf:"bytes,1,rep,name=volumes"`<br>
<br>
InitContainers []Container `json:"initContainers,omitempty" patchStrategy:"merge" patchMergeKey:"name" protobuf:"bytes,20,rep,name=initContainers"`<br>
<br>
Containers []Container `json:"containers" patchStrategy:"merge" patchMergeKey:"name" protobuf:"bytes,2,rep,name=containers"`<br>
<br>
EphemeralContainers []EphemeralContainer `json:"ephemeralContainers,omitempty" patchStrategy:"merge" patchMergeKey:"name" protobuf:"bytes,34,rep,name=ephemeralContainers"`<br>
<br>
RestartPolicy RestartPolicy `json:"restartPolicy,omitempty" protobuf:"bytes,3,opt,name=restartPolicy,casttype=RestartPolicy"`<br>
<br>
...<br>
&#125; <br>
</pre><br>
Kubernetes中定义的所有结构k8s.io/api模块自带JSON和Protobuf注解。但要注意：<br>
<ul><li>支持将数据编组成JSON。</li><li>Protobuf序列化是不被鼓励的——产生的结果可能与现有的API服务器不兼容（更多信息请参阅<a href="https://github.com/kubernetes/api/tree/35d41aaac2bf55a353ccade31b852d466b2495c2#recommended-use">README</a>）。</li></ul><br>
<br><blockquote><br>专业提示：如果你去阅读源码，你会看到k8s.io/apimachery通过对提供的对象调用标准的json.marshal()来实现JSON的序列化。因此，不要害怕，只要需要转储API对象，就使用json.Marshal()。</blockquote>总结一下，k8s.io/api模块：<br>
<ul><li>巨大——1000个以上的结构描述Kubernetes API对象。</li><li>简单——几乎没有算法，只有“哑”的数据结构。</li><li>有用——它的数据类型被客户端、服务器、控制器等使用。</li></ul><br>
<br><h3>k8s.io/apimachinery模块</h3>不像简单的k8s.io/api模块，k8s.io/apimachery模块是相当复杂的。<a href="https://github.com/kubernetes/apimachinery/tree/3d7c63b4de4fdee1917284129969901d4777facc#purpose">README</a>将其目的描述为：<br>
<br>这个库是服务器和客户端使用Kubernetes API基础设施的共享依赖项，不需要直接的类型依赖项。它的第一批消费者是k8s.io/kubernetes、k8s.io/client-go、k8s.io/apiserver。<br>
<br>要在一篇文章中涵盖apimachinery模块的所有职责是很困难的。因此，我将讨论这个模块中最常见的包、类型和功能。<br>
<h4>有用的结构和接口</h4>k8s.io/api模块专注于具体的高级类型，如Deployment、Secret、Pod，k8s.io/apimachery是低层但更通用的数据结构。<br>
<br>例如，Kubernetes对象的所有这些公共属性：apiVersion、kind、name、uid、ownerReferences、creationTimestamp等。如果我要构建自己的Kubernetes自定义资源，我就不需要自己为这些属性定义数据类型——这要感谢apimachery模块。<br>
<br>k8s.io/apimachery/pkg/apis/meta包定义了两个方便的结构体：TypeMeta和ObjectMeta，它们可以嵌入到用户定义的结构体中，使其看起来像任何其他Kubernetes对象。<br>
<br>此外，TypeMeta和ObjectMeta结构实现了meta.Type和meta.Object接口，可用于以通用方式指向任何兼容对象。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220417/e3434cf74ecfe7c49f6b5e0c4849bd3b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220417/e3434cf74ecfe7c49f6b5e0c4849bd3b.png" class="img-polaroid" title="03.png" alt="03.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在apimachery模块中定义的另一个方便的类型是接口runtime.Object。由于其简单的定义，它可能看起来毫无用处：<br>
<pre class="prettyprint">// pkg/runtime<br>
<br>
type Object interface &#123;<br>
GetObjectKind() schema.ObjectKind<br>
DeepCopyObject() Object<br>
&#125; <br>
</pre><br>
但实际上，它被用得很多！Kubernetes的代码是在Go获得真正泛型支持之前很久编写的。因此，runtime.Object很像传统的接口——它是一个泛型接口，在代码库中广泛地进行类型断言和类型切换。而实际的类型可以通过检查底层对象的类型来获得。<br>
<br><blockquote><br>runtime.Object实例可以指向任何具有kind属性的对象——成熟的Kubernetes对象、不携带元数据的更简单的API资源，或者具有定义良好的对象方案的任何其他类型的对象。<br>
  <br>
  <br>注意，虽然看起来相似，但meta.Object不能安全地向下转换到相应的Kubernetes对象，因为它的结构偏移量不为零。</blockquote>更有用的apimachery类型：<br>
<ul><li>PartialObjectMetadata结构——meta.TypeMeta和meta.ObjectMeta作为一种通用的方法来表示任何具有元数据的对象。</li><li>APIVersions、APIGroupList、APIGroup结构体——还记得kubectl get的<a href="http://dockone.io/article/2434812">API探索练习吗</a>？原始API这些和类似的结构用于Kubernetes，API资源的类型，但不是Kubernetes对象（例如，它们有kind和apiVersion属性，但没有真正的Object元数据）。</li><li>GetOptions、ListOptions、UpdateOptions等等——这些结构体代表了客户端对资源的相应动作的参数。</li><li>GroupKind、GroupVersionKind、GroupResource、GroupVersionResource等——简单的数据传输对象，包含组、版本、类型或资源字符串的元组。</li></ul><br>
<br>在讨论Scheme和RESTMapper之前，请记住GroupVersionKind和GroupVersionResource——他们的知识将派上用场。<br>
<h4>非结构化的结构</h4>是的，你没听错。撇开玩笑不谈，它是另一种重要且广泛使用的数据类型。<br>
<br>使用固定k8s.io/api类型处理Kubernetes对象很方便，但如果：<br>
<ul><li>你需要以通用的方式使用Kubernetes对象？</li><li>你不想或不能依赖于API模块？</li><li>你需要使用API模块中没有定义的自定义资源？</li></ul><br>
<br>非结构化，用于救援的非结构化结构！这个结构体允许没有注册Go结构体的对象被操作为通用的JSON类对象：<br>
<pre class="prettyprint">type Unstructured struct &#123;<br>
// Object is a JSON compatible map with<br>
// string, float, int, bool, []interface&#123;&#125;, or<br>
// map[string]interface&#123;&#125; children.<br>
Object map[string]interface&#123;&#125;<br>
&#125;<br>
<br>
// And for the list of objects you can <br>
// use the UnstructuredList struct.<br>
type UnstructuredList struct &#123;<br>
Object map[string]interface&#123;&#125;<br>
<br>
Items []Unstructured<br>
&#125; <br>
</pre><br>
实际上，这两个结构只是map[string]interface&#123;&#125;。不过，它们附带了一堆方便的方法，简化了嵌套属性访问和JSON序列化/反序列化。<br>
<br>示例：<a href="https://github.com/iximiuz/client-go-examples/blob/5b220c4572d65ea8bf0ad68e369e015902e7521c/crud-dynamic-simple/main.go#L36" rel="nofollow" target="_blank">https://github.com/iximiuz/cli ... 23L36</a><br>
<h4>类型转换——非结构化到类型化，反之亦然</h4>自然的，需要将非结构化对象转换为具体k8s.io/api类型（反之亦然）。runtime.UnstructuredConverter接口及其默认实现DefaultUnstructuredConverter可以帮助你：<br>
<pre class="prettyprint">type UnstructuredConverter interface &#123;<br>
ToUnstructured(obj interface&#123;&#125;) (map[string]interface&#123;&#125;, error)<br>
FromUnstructured(u map[string]interface&#123;&#125;, obj interface&#123;&#125;) error<br>
&#125; <br>
</pre><br>
示例：<a href="https://github.com/iximiuz/client-go-examples/tree/main/convert-unstructured-typed" rel="nofollow" target="_blank">https://github.com/iximiuz/cli ... typed</a><br>
<h4>对象序列化为JSON、YAML或Protobuf</h4>在处理来自静态类型语言的API时，另一项乏味的任务是将数据结构编组和解组到它们的连线表示中。<br>
<br>大量的apimachery代码都用于此任务：<br>
<pre class="prettyprint">// pkg/runtime<br>
<br>
// Encoder writes objects to a serialized form<br>
type Encoder interface &#123;<br>
Encode(obj Object, w io.Writer) error<br>
Identifier() Identifier<br>
&#125;<br>
<br>
// Decoder attempts to load an object from data.<br>
type Decoder interface &#123;<br>
Decode(<br>
data []byte,<br>
defaults *schema.GroupVersionKind,<br>
into Object<br>
) (Object, *schema.GroupVersionKind, error)<br>
&#125;<br>
<br>
type Serializer interface &#123;<br>
Encoder<br>
Decoder<br>
&#125; <br>
</pre><br>
注意到上面的代码片段中的这些对象了吗？是的，这些是runtime.Object，也就是Kind-able接口实例。<br>
<br>例子:<br>
<ol><li><a href="https://github.com/iximiuz/client-go-examples/tree/main/serialize-typed-json" rel="nofollow" target="_blank">https://github.com/iximiuz/cli ... -json</a></li><li><a href="https://github.com/iximiuz/client-go-examples/tree/main/serialize-typed-yaml" rel="nofollow" target="_blank">https://github.com/iximiuz/cli ... -yaml</a></li><li><a href="https://github.com/iximiuz/client-go-examples/tree/main/serialize-unstructured-json" rel="nofollow" target="_blank">https://github.com/iximiuz/cli ... -json</a></li><li><a href="https://github.com/iximiuz/client-go-examples/tree/main/serialize-unstructured-yaml" rel="nofollow" target="_blank">https://github.com/iximiuz/cli ... -yaml</a></li></ol><br>
<br><h4>模式和RESTMapper</h4>runtime.Schema在使用client-go时，模式概念随处出现，特别是在编写处理自定义资源的控制器（或操作符）时。<br>
<br>我花了一段时间才明白它的目的。但是，按照正确的顺序处理事情会有所帮助。<br>
<br>考虑一下非结构化到类型化转换的潜在实现：有一个类似json的对象，以及一些具体k8s.io/api类型需要从它创建。也许，第一步就是要弄清楚如何使用kind字符串创建一个空的类型化对象实例。<br>
<br>一个简单的方法可能看起来像一个巨大的switch语句，覆盖所有可能的类型（实际上是API组）：<br>
<pre class="prettyprint">import (<br>
appsv1 "k8s.io/api/apps/v1"<br>
corev1 "k8s.io/api/core/v1"<br>
)<br>
<br>
func New(apiVersion, kind string) runtime.Object &#123;<br>
switch (apiVersion + "/" + kind) &#123;  <br>
case: "v1/Pod":<br>
return &corev1.Pod&#123;&#125;<br>
case: "apps/v1/Deployment":<br>
return &appsv1.Deployment&#123;&#125;<br>
&#125;<br>
...<br>
&#125; <br>
</pre><br>
更聪明的方法是使用反射。不是开关，而是映射[字符串]反射。类型可以为所有注册类型维护：<br>
<pre class="prettyprint">type Registry struct &#123;<br>
map[string]reflect.Type types<br>
&#125;<br>
<br>
func (r *Registry) Register(apiVersion, kind string, typ reflect.Type) &#123;<br>
r.types[apiVersion + "/" + kind] = typ<br>
&#125;<br>
<br>
func (r *Registry) New(apiVersion, kind string) runtime.Object &#123;<br>
return r.types[apiVersion + "/" + kind].New().(runtime.Object)<br>
&#125; <br>
</pre><br>
这种方法的优点是不需要生成代码，并且可以在运行时添加新的类型映射。<br>
<br>现在，考虑一个反序列化问题：需要将一段YAML或JSON转换为一个类型化对象。第一步——对象创建——将非常类似。<br>
<br>事实证明，通过API组和类型创建空对象是一项非常频繁的任务，以至于它在apimachery模块——运行时中获得了自己的模块——runtime.Schema：<br>
<pre class="prettyprint">// Scheme defines methods for serializing and deserializing API objects, a type<br>
// registry for converting group, version, and kind information to and from Go<br>
// schemas, and mappings between Go schemas of different versions. <br>
type Scheme struct &#123;<br>
gvkToType map[schema.GroupVersionKind]reflect.Type<br>
<br>
typeToGVK map[reflect.Type][]schema.GroupVersionKind<br>
<br>
unversionedTypes map[reflect.Type]schema.GroupVersionKind<br>
<br>
unversionedKinds map[string]reflect.Type<br>
<br>
...<br>
&#125; <br>
</pre><br>
runtime.Scheme结构就是这样一个注册表，它包含了所有Kubernetes对象的kind到type和type到kind的映射。<br>
<br><blockquote><br>记住，GroupVersionKind只是一个元组，即DTO结构，对吗？</blockquote>runtime.Scheme结构实际上是非常强大的，它有一大堆方法和实现一些基本的接口，如：<br>
<pre class="prettyprint">// ObjectTyper contains methods for extracting <br>
// the APIVersion and Kind of objects.<br>
type ObjectTyper interface &#123;<br>
ObjectKinds(runtime.Object) ([]schema.GroupVersionKind, bool, error)<br>
Recognizes(gvk schema.GroupVersionKind) bool<br>
&#125;<br>
<br>
// ObjectCreater contains methods for instantiating<br>
// an object by kind and version.<br>
type ObjectCreater interface &#123;<br>
New(kind schema.GroupVersionKind) (out Object, err error)<br>
&#125; <br>
</pre><br>
然而，runtime.Schema不是万能的。它有从kind到type的映射，但是如果不是只有资源名已知而不是类型呢?<br>
<br>这就是RESTMapper的作用所在：<br>
<pre class="prettyprint">type RESTMapper interface &#123;<br>
// KindFor takes a partial resource and returns the single match.  Returns an error if there are multiple matches<br>
KindFor(resource schema.GroupVersionResource) (schema.GroupVersionKind, error)<br>
<br>
// KindsFor takes a partial resource and returns the list of potential kinds in priority order<br>
KindsFor(resource schema.GroupVersionResource) ([]schema.GroupVersionKind, error)<br>
<br>
...<br>
<br>
ResourceSingularizer(resource string) (singular string, err error)<br>
&#125; <br>
</pre><br>
RESTMapper也是某种注册表。但是，它维护资源到种类的映射。因此，向映射器提供一个像apps/v1/Deployment这样的字符串，就会得到API Group apps/v1和部署类型。RESTMapper还可以处理资源快捷方式和奇点化: po、pod和pods可以注册为相同资源的别名。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220417/fdaa6993f7eebfbfe4d32c4fe9d711e2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220417/fdaa6993f7eebfbfe4d32c4fe9d711e2.png" class="img-polaroid" title="04.png" alt="04.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通常情况下，会有一个全局的单例运行时。然而，似乎apimachery模块本身试图避免状态——它定义了RESTMapper和Scheme结构，但没有实例化它们。<br>
<br>不像运行时。该方案被apimachery模块本身广泛使用，RESTMapper在内部没有使用，至少目前没有。<br>
<h4>字段和标签选择器</h4>字段和标签的类型、创建和匹配逻辑也存在于apimachery模块中。例如，这里是k8s.io/apimachinery/pkg/labels包：<br>
<pre class="prettyprint">lbl := labels.Set&#123;"foo": "bar"&#125;<br>
sel, _ = labels.Parse("foo==bar")<br>
if sel.Matches(lbl) &#123;<br>
fmt.Printf("Selector %v matched label set %v\n", sel, lbl)<br>
&#125; <br>
</pre><br>
例子:<br>
<ol><li><a href="https://github.com/iximiuz/client-go-examples/tree/main/label-selectors" rel="nofollow" target="_blank">https://github.com/iximiuz/cli ... ctors</a></li><li><a href="https://github.com/iximiuz/client-go-examples/tree/main/field-selectors" rel="nofollow" target="_blank">https://github.com/iximiuz/cli ... ctors</a></li></ol><br>
<br><h4>API错误处理</h4>在代码中使用Kubernetes API是不可能的，除非正确处理它的错误。API服务器可能完全消失，请求可能未经授权，对象可能丢失，并发更新可能发生冲突。幸运的是，k8s.io/apimachery /pkg/api/errors包定义了一些方便的实用函数来处理API错误。下面是一个例子：<br>
<pre class="prettyprint">_, err = client.<br>
CoreV1().<br>
ConfigMaps("default").<br>
Get(<br>
context.Background(),<br>
"this_name_definitely_does_not_exist",<br>
metav1.GetOptions&#123;&#125;,<br>
)<br>
if !errors.IsNotFound(err) &#123;<br>
panic(err.Error())<br>
&#125; <br>
</pre><br>
示例：<a href="https://github.com/iximiuz/client-go-examples/tree/main/error-handling" rel="nofollow" target="_blank">https://github.com/iximiuz/cli ... dling</a><br>
<h4>其他</h4>最后但并非最不重要的是，apimachery/pkg/util包充满了有用的东西。下面是一些例子:<br>
<ul><li>util/wait包通过重试和适当的backoff/jitter实现，减轻了等待资源出现或消失的任务。</li><li>util/yaml有助于对yaml进行反序列化或将其转换为JSON。</li></ul><br>
<br><h3>总结</h3>k8s.io/api和k8s.io/apimachery包是学习如何在Go中使用Kubernetes对象的一个很好的起点。如果你需要编写你的第一个控制器，直接跳到client-go，甚至跳到controller-runtime或kubebuilder可能会让你的学习经历变得太复杂——可能会有太多的知识缺口。不过，先看看API和apimachery包，然后再尝试一下，这将帮助你在接下来的旅程中保持平和的心态。<br>
<h3>请继续关注</h3>已经有三篇文章了，我还没接触过客户端。下次，我保证会是一篇关于客户端的文章！<br>
<br><strong>原文链接：<a href="https://iximiuz.com/en/posts/kubernetes-api-go-types-and-common-machinery/">How To Call Kubernetes API using Go - Types and Common Machinery</a></strong><br>
<br><strong>译者</strong>：Mr.lzc，高级工程师、DevOpsDays、HDZ深圳核心组织者，目前供职于华为，从事云计算工作，专注于Kubernetes、微服务领域。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            