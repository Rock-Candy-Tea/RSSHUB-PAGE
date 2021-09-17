
---
title: '如何高效掌控 Kubernetes 资源变化？Kubernetes Informer 实现机制浅析'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210915/52e4282b2d8a654449515e509a705ac5.png'
author: Dockone
comments: false
date: 2021-09-17 05:07:34
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210915/52e4282b2d8a654449515e509a705ac5.png'
---

<div>   
<br><h3>概述</h3>进入 Kubernetes 的世界，会发现有很多的 Controller，它们都是为了完成某类资源（如 Pod 是通过 DeploymentController，ReplicaSetController 进行管理）的调谐，目标是<strong>保持用户期望的状态</strong>。<br>
<br>Kubernetes 中有几十种类型的资源，如何能<strong>让 Kubernetes 内部以及外部用户方便、高效的获取某类资源的变化</strong>，就是本文 Informer 要实现的。本文将从 Reflector（反射器）、DeltaFIFO（增量队列）、Indexer（索引器）、Controller（控制器）、SharedInformer（共享资源通知器）、ProcessorListener（事件监听处理器）、Workqueue（事件处理工作队列）等方面进行解析。<br>
<br><blockquote><br>本文及后续相关文章都基于 Kubernetes v1.22。</blockquote><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210915/52e4282b2d8a654449515e509a705ac5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210915/52e4282b2d8a654449515e509a705ac5.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>K8s-informer</em><br>
<h3>从 Reflector 说起</h3>Reflector 的主要职责是从 API Server 拉取并持续监听（ListAndWatch）相关资源类型的增删改（Add/Update/Delete）事件，存储在由 DeltaFIFO 实现的本地缓存（local Store）中。<br>
<br>首先看一下 Reflector 结构体定义：<br>
<pre class="prettyprint">// staging/src/k8s.io/client-go/tools/cache/reflector.go<br>
type Reflector struct &#123;<br>
// 通过 file:line 唯一标识的 name<br>
name string<br>
<br>
// 下面三个为了确认类型<br>
expectedTypeName string<br>
expectedType     reflect.Type<br>
expectedGVK      *schema.GroupVersionKind<br>
<br>
// 存储 interface: 具体由 DeltaFIFO 实现存储<br>
store Store<br>
// 用来从 API Server 拉取全量和增量资源<br>
listerWatcher ListerWatcher<br>
<br>
// 下面两个用来做失败重试<br>
backoffManager         wait.BackoffManager<br>
initConnBackoffManager wait.BackoffManager<br>
<br>
// informer 使用者重新同步的周期<br>
resyncPeriod time.Duration<br>
// 判断是否满足可以重新同步的条件<br>
ShouldResync func() bool<br>
<br>
clock clock.Clock<br>
<br>
// 是否要进行分页 List<br>
paginatedResult bool<br>
<br>
// 最后同步的资源版本号，以此为依据，watch 只会监听大于此值的资源<br>
lastSyncResourceVersion string<br>
// 最后同步的资源版本号是否可用<br>
isLastSyncResourceVersionUnavailable bool<br>
// 加把锁控制版本号<br>
lastSyncResourceVersionMutex sync.RWMutex<br>
<br>
// 每页大小<br>
WatchListPageSize int64<br>
// watch 失败回调 handler<br>
watchErrorHandler WatchErrorHandler<br>
&#125; <br>
</pre><br>
从结构体定义可以看到，通过<strong>指定目标资源类型进行 ListAndWatch，并可进行分页相关设置</strong>。<br>
<br>第一次拉取全量资源（目标资源类型）后通过 syncWith 函数全量替换（Replace）到 DeltaFIFO queue/items 中，之后通过持续监听 Watch（目标资源类型）增量事件，并去重更新到 DeltaFIFO queue/items 中，等待被消费。<br>
<br>watch 目标类型通过 Go reflect 反射实现如下：<br>
<pre class="prettyprint">// staging/src/k8s.io/client-go/tools/cache/reflector.go<br>
// watchHandler watches w and keeps *resourceVersion up to date.<br>
func (r *Reflector) watchHandler(start time.Time, w watch.Interface, resourceVersion *string, errc chan error, stopCh <-chan struct&#123;&#125;) error &#123;<br>
<br>
...<br>
if r.expectedType != nil &#123;<br>
if e, a := r.expectedType, reflect.TypeOf(event.Object); e != a &#123;<br>
utilruntime.HandleError(fmt.Errorf("%s: expected type %v, but watch event object had type %v", r.name, e, a))<br>
continue<br>
&#125;<br>
&#125;<br>
if r.expectedGVK != nil &#123;<br>
if e, a := *r.expectedGVK, event.Object.GetObjectKind().GroupVersionKind(); e != a &#123;<br>
utilruntime.HandleError(fmt.Errorf("%s: expected gvk %v, but watch event object had gvk %v", r.name, e, a))<br>
continue<br>
&#125;<br>
&#125;<br>
...<br>
&#125; <br>
</pre><br>
<br><blockquote><br>通过反射确认目标资源类型，所以命名为 Reflector 还是比较贴切的；List/Watch 的目标资源类型在 NewSharedIndexInformer.ListerWatcher 进行了确定，但 Watch 还会在 watchHandler 中再次比较一下目标类型。</blockquote><h3>认识 DeltaFIFO</h3>还是先看下 DeltaFIFO 结构体定义：<br>
<pre class="prettyprint">// staging/src/k8s.io/client-go/tools/cache/delta_fifo.go<br>
type DeltaFIFO struct &#123;<br>
// 读写锁、条件变量<br>
lock sync.RWMutex<br>
cond sync.Cond<br>
<br>
// KV 存储：objKey1->Deltas[obj1-Added, obj1-Updated...]<br>
items map[string]Deltas<br>
<br>
// 只存储所有 objKeys<br>
queue []string<br>
<br>
// 是否已经填充：通过 Replace() 接口将第一批对象放入队列，或者第一次调用增、删、改接口时标记为true<br>
populated bool<br>
// 通过 Replace() 接口将第一批对象放入队列的数量<br>
initialPopulationCount int<br>
<br>
// keyFunc 用来从某个 obj 中获取其对应的 objKey<br>
keyFunc KeyFunc<br>
<br>
// 已知对象，其实就是 Indexer<br>
knownObjects KeyListerGetter<br>
<br>
// 队列是否已经关闭<br>
closed bool<br>
<br>
// 以 Replaced 类型发送（为了兼容老版本的 Sync）<br>
emitDeltaTypeReplaced bool<br>
&#125; <br>
</pre><br>
DeltaType 可分为以下类型：<br>
<pre class="prettyprint">// staging/src/k8s.io/client-go/tools/cache/delta_fifo.go<br>
type DeltaType string<br>
<br>
const (<br>
Added   DeltaType = "Added"<br>
Updated DeltaType = "Updated"<br>
Deleted DeltaType = "Deleted"<br>
Replaced DeltaType = "Replaced" // 第一次或重新同步<br>
Sync DeltaType = "Sync" // 老版本重新同步叫 Sync<br>
)<br>
</pre><br>
通过上面的 Reflector 分析可以知道，<strong>DeltaFIFO 的职责</strong>是通过队列加锁处理（queueActionLocked）、去重（dedupDeltas）、存储在由 DeltaFIFO 实现的本地缓存（local Store）中，包括 queue（仅存 objKeys）和 items（存 objKeys 和对应的 Deltas 增量变化），并通过 Pop 不断消费，通过 Process（item）处理相关逻辑。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210915/3955bd7252bda7a15a2f20014b0c1c0d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210915/3955bd7252bda7a15a2f20014b0c1c0d.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>K8s-DeltaFIFO</em><br>
<h3>索引 Indexer</h3>上一步 ListAndWatch 到的资源已经存储到 DeltaFIFO 中，接着调用 Pop 从队列进行消费。实际使用中，Process 处理函数由 sharedIndexInformer.HandleDeltas 进行实现。HandleDeltas 函数根据上面不同的 DeltaType 分别进行 Add/Update/Delete，并同时创建、更新、删除对应的索引。<br>
<br>具体索引实现如下：<br>
<pre class="prettyprint">// staging/src/k8s.io/client-go/tools/cache/index.go<br>
// map 索引类型 => 索引函数<br>
type Indexers map[string]IndexFunc<br>
<br>
// map 索引类型 => 索引值 map<br>
type Indices map[string]Index<br>
<br>
// 索引值 map: 由索引函数计算所得索引值(indexedValue) => [objKey1, objKey2...]<br>
type Index map[string]sets.String<br>
</pre><br>
<strong>索引函数（IndexFunc）</strong>：就是计算索引的函数，这样允许扩展多种不同的索引计算函数。默认也是最常用的索引函数是：MetaNamespaceIndexFunc。<br>
<br><strong>索引值（indexedValue）</strong>：有些地方叫 indexKey，表示由索引函数（IndexFunc）计算出来的索引值（如 ns1）。<br>
<br><strong>对象键（objKey）</strong>：对象 obj 的 唯一 key（如 ns1/pod1），与某个资源对象一一对应。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210915/828f25a241a8c38c8d6f3b86a6d0798a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210915/828f25a241a8c38c8d6f3b86a6d0798a.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>K8s-indexer</em><br>
<br>可以看到，Indexer 由 ThreadSafeStore 接口集成，最终由 threadSafeMap 实现。<br>
<br><blockquote><br>索引函数 IndexFunc（如 MetaNamespaceIndexFunc）、KeyFunc（如 MetaNamespaceKeyFunc）区别：前者表示如何计算索引，后者表示如何获取对象键（objKey）；<br>
  <br>
  <br>索引键（indexKey，有些地方是 indexedValue）、对象键（objKey）区别：前者表示由索引函数（IndexFunc）计算出来的索引键（如 ns1），后者则是 obj 的 唯一 key（如 ns1/pod1）。</blockquote><h3>总管家 Controller</h3>Controller 作为核心中枢，集成了上面的组件 Reflector、DeltaFIFO、Indexer、Store，成为连接下游消费者的桥梁。<br>
<br>Controller 由 controller 结构体进行具体实现：<br>
<br><blockquote><br>在 Kubernetes 中约定俗成：大写定义的 interface 接口，由对应小写定义的结构体进行实现。</blockquote><pre class="prettyprint">// staging/src/k8s.io/client-go/tools/cache/controller.go<br>
type controller struct &#123;<br>
config         Config<br>
reflector      *Reflector // 上面已分析的组件<br>
reflectorMutex sync.RWMutex<br>
clock          clock.Clock<br>
&#125;<br>
<br>
type Config struct &#123;<br>
// 实际由 DeltaFIFO 实现<br>
Queue<br>
<br>
// 构造 Reflector 需要<br>
ListerWatcher<br>
<br>
// Pop 出来的 obj 处理函数<br>
Process ProcessFunc<br>
<br>
// 目标对象类型<br>
ObjectType runtime.Object<br>
<br>
// 全量重新同步周期<br>
FullResyncPeriod time.Duration<br>
<br>
// 是否进行重新同步的判断函数<br>
ShouldResync ShouldResyncFunc<br>
<br>
// 如果为 true，Process() 函数返回 err，则再次入队 re-queue<br>
RetryOnError bool<br>
<br>
// Watch 返回 err 的回调函数<br>
WatchErrorHandler WatchErrorHandler<br>
<br>
// Watch 分页大小<br>
WatchListPageSize int64<br>
&#125; <br>
</pre><br>
Controller 中以 goroutine 协程方式启动 Run 方法，会启动 Reflector 的 ListAndWatch()，用于从 API Server 拉取全量和监听增量资源，存储到 DeltaFIFO。接着，启动 processLoop 不断从 DeltaFIFO Pop 进行消费。在 sharedIndexInformer 中 Pop 出来进行处理的函数是 HandleDeltas，一方面维护 Indexer 的 Add/Update/Delete，另一方面调用下游 sharedProcessor 进行 handler 处理。<br>
<h3>启动 SharedInformer</h3>SharedInformer 接口由 SharedIndexInformer 进行集成，由 sharedIndexInformer（这里看到了吧，又是大写定义的 interface 接口，由对应小写定义的结构体进行实现）进行实现。<br>
<br>看一下结构体定义：<br>
<pre class="prettyprint">// staging/src/k8s.io/client-go/tools/cache/shared_informer.go  <br>
type SharedIndexInformer interface &#123;  <br>
SharedInformer  <br>
// AddIndexers add indexers to the informer before it starts.  <br>
AddIndexers(indexers Indexers) error  <br>
GetIndexer() Indexer  <br>
&#125;  <br>
<br>
type sharedIndexInformer struct &#123;  <br>
indexer Indexer  <br>
controller Controller  <br>
<br>
// 处理函数，将是重点  <br>
processor *sharedProcessor  <br>
<br>
// 检测 cache 是否有变化，一把用作调试，默认是关闭的  <br>
cacheMutationDetector MutationDetector  <br>
<br>
// 构造 Reflector 需要  <br>
listerWatcher ListerWatcher  <br>
<br>
// 目标类型，给 Reflector 判断资源类型  <br>
objectType runtime.Object  <br>
<br>
// Reflector 进行重新同步周期  <br>
resyncCheckPeriod time.Duration  <br>
<br>
// 如果使用者没有添加 Resync 时间，则使用这个默认的重新同步周期  <br>
defaultEventHandlerResyncPeriod time.Duration  <br>
clock clock.Clock  <br>
<br>
// 两个 bool 表达了三个状态：controller 启动前、已启动、已停止  <br>
started, stopped bool  <br>
startedLock sync.Mutex  <br>
<br>
// 当 Pop 正在消费队列，此时新增的 listener 需要加锁，防止消费混乱  <br>
blockDeltas sync.Mutex  <br>
<br>
// Watch 返回 err 的回调函数  <br>
watchErrorHandler WatchErrorHandler  <br>
&#125;  <br>
<br>
type sharedProcessor struct &#123;  <br>
listenersStarted bool  <br>
listenersLock sync.RWMutex  <br>
listeners []*processorListener  <br>
syncingListeners []*processorListener // 需要 sync 的 listeners  <br>
clock clock.Clock  <br>
wg wait.Group  <br>
&#125; <br>
</pre><br>
从结构体定义可以看到，通过集成的 controller(上面已分析) 进行 Reflector ListAndWatch，并存储到 DeltaFIFO，并启动 Pop 消费队列，在 sharedIndexInformer 中 Pop 出来进行处理的函数是 HandleDeltas。<br>
<br>所有的 listeners 通过 sharedIndexInformer.AddEventHandler 加入到 processorListener 数组切片中，并通过判断当前 controller 是否已启动做不同处理如下：<br>
<pre class="prettyprint">// staging/src/k8s.io/client-go/tools/cache/shared_informer.go<br>
func (s *sharedIndexInformer) AddEventHandlerWithResyncPeriod(handler ResourceEventHandler, resyncPeriod time.Duration) &#123;<br>
...<br>
<br>
// 如果还没有启动，则直接 addListener 加入即可返回<br>
if !s.started &#123;<br>
s.processor.addListener(listener)<br>
return<br>
&#125;<br>
<br>
// 加锁控制<br>
s.blockDeltas.Lock()<br>
defer s.blockDeltas.Unlock()<br>
<br>
s.processor.addListener(listener)<br>
<br>
// 遍历所有对象，发送到刚刚新加入的 listener<br>
for _, item := range s.indexer.List() &#123;<br>
listener.add(addNotification&#123;newObj: item&#125;)<br>
&#125;<br>
&#125; <br>
</pre><br>
接着，在 HandleDeltas 中，根据 obj 的 Delta 类型（Added/Updated/Deleted/Replaced/Sync）调用 sharedProcessor.distribute 给所有监听 listeners 处理。<br>
<h3>注册 SharedInformerFactory</h3>SharedInformerFactory 作为使用 SharedInformer 的工厂类，提供了高内聚低耦合的工厂类设计模式，其结构体定义如下：<br>
<pre class="prettyprint">// staging/src/k8s.io/client-go/informers/factory.go<br>
type SharedInformerFactory interface &#123;<br>
internalinterfaces.SharedInformerFactory // 重点内部接口<br>
ForResource(resource schema.GroupVersionResource) (GenericInformer, error)<br>
WaitForCacheSync(stopCh <-chan struct&#123;&#125;) map[reflect.Type]bool<br>
<br>
Admissionregistration() admissionregistration.Interface<br>
Internal() apiserverinternal.Interface<br>
Apps() apps.Interface<br>
Autoscaling() autoscaling.Interface<br>
Batch() batch.Interface<br>
Certificates() certificates.Interface<br>
Coordination() coordination.Interface<br>
Core() core.Interface<br>
Discovery() discovery.Interface<br>
Events() events.Interface<br>
Extensions() extensions.Interface<br>
Flowcontrol() flowcontrol.Interface<br>
Networking() networking.Interface<br>
Node() node.Interface<br>
Policy() policy.Interface<br>
Rbac() rbac.Interface<br>
Scheduling() scheduling.Interface<br>
Storage() storage.Interface<br>
&#125;<br>
<br>
// staging/src/k8s.io/client-go/informers/internalinterfaces/factory_interfaces.go<br>
type SharedInformerFactory interface &#123;<br>
Start(stopCh <-chan struct&#123;&#125;) // 启动 SharedIndexInformer.Run<br>
InformerFor(obj runtime.Object, newFunc NewInformerFunc) cache.SharedIndexInformer // 目标类型初始化<br>
&#125; <br>
</pre><br>
以 PodInformer 为例，说明使用者如何构建自己的 Informer，PodInformer 定义如下：<br>
<pre class="prettyprint">// staging/src/k8s.io/client-go/informers/core/v1/pod.go<br>
type PodInformer interface &#123;<br>
Informer() cache.SharedIndexInformer<br>
Lister() v1.PodLister<br>
&#125;<br>
<br>
由小写的 podInformer 实现（又看到了吧，大写接口小写实现的 Kubernetes 风格）：<br>
<br>
type podInformer struct &#123;<br>
factory          internalinterfaces.SharedInformerFactory<br>
tweakListOptions internalinterfaces.TweakListOptionsFunc<br>
namespace        string<br>
&#125;<br>
<br>
func (f *podInformer) defaultInformer(client kubernetes.Interface, resyncPeriod time.Duration) cache.SharedIndexInformer &#123;<br>
return NewFilteredPodInformer(client, f.namespace, resyncPeriod, cache.Indexers&#123;cache.NamespaceIndex: cache.MetaNamespaceIndexFunc&#125;, f.tweakListOptions)<br>
&#125;<br>
<br>
func (f *podInformer) Informer() cache.SharedIndexInformer &#123;<br>
return f.factory.InformerFor(&corev1.Pod&#123;&#125;, f.defaultInformer)<br>
&#125;<br>
<br>
func (f *podInformer) Lister() v1.PodLister &#123;<br>
return v1.NewPodLister(f.Informer().GetIndexer())<br>
&#125; <br>
</pre><br>
由使用者传入目标类型（&corev1.Pod&#123;&#125;）、构造函数（defaultInformer），调用 SharedInformerFactory.InformerFor 实现目标 Informer 的注册，然后调用 SharedInformerFactory.Start 进行 Run，就启动了上面分析的  <strong>SharedIndexedInformer -> Controller -> Reflector -> DeltaFIFO 流程。</strong><br>
<br><blockquote><br>通过使用者自己传入目标类型、构造函数进行 Informer 注册，实现了 SharedInformerFactory 高内聚低耦合的设计模式。</blockquote><h3>回调 ProcessorListener</h3>所有的 listerners 由 ProcessorListener 实现，分为两组：listeners，syncingListeners，分别遍历所属组全部 listeners，将数据投递到 processorListener 进行处理。<br>
<br><blockquote><br>因为各 listeners 设置的 resyncPeriod 可能不一致，所以将没有设置（resyncPeriod = 0）的归为 listeners 组，将设置了 resyncPeriod 的归到 syncingListeners 组。<br>
  <br>
  <br>如果某个 listener 在多个地方（sharedIndexInformer.resyncCheckPeriod, sharedIndexInformer.AddEventHandlerWithResyncPeriod）都设置了 resyncPeriod，则取最小值 minimumResyncPeriod。</blockquote><pre class="prettyprint">// staging/src/k8s.io/client-go/tools/cache/shared_informer.go<br>
func (p *sharedProcessor) distribute(obj interface&#123;&#125;, sync bool) &#123;<br>
p.listenersLock.RLock()<br>
defer p.listenersLock.RUnlock()<br>
<br>
if sync &#123;<br>
for _, listener := range p.syncingListeners &#123;<br>
listener.add(obj)<br>
&#125;<br>
&#125; else &#123;<br>
for _, listener := range p.listeners &#123;<br>
listener.add(obj)<br>
&#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
从代码可以看到 processorListener 巧妙地使用了两个 channel（addCh，nextCh）和一个 pendingNotifications（由 slice 实现的滚动 Ring）进行 buffer 缓冲，默认的 initialBufferSize = 1024。既做到了高效传递数据，又不阻塞上下游处理，值得学习。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210915/9eacce16a4adc67014d4758a478c7e56.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210915/9eacce16a4adc67014d4758a478c7e56.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>K8s-processorListener</em><br>
<h3>Workqueue 忙起来</h3>通过上一步 processorListener 回调函数，交给内部 ResourceEventHandler 进行真正的增删改（CUD）处理，分别调用 OnAdd/OnUpdate/OnDelete 注册函数进行处理。<br>
<br>为了<strong>快速处理而不阻塞 processorListener 回调函数，一般使用 Workqueue 进行异步化解耦合处理</strong>，其实现如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210915/03065bcb65631b4e286e43435aaa40b3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210915/03065bcb65631b4e286e43435aaa40b3.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>K8s-workqueue</em><br>
<br>从图中可以看到，workqueue.RateLimitingInterface 集成了 DelayingInterface，DelayingInterface 集成了 Interface，最终由 rateLimitingType 进行实现，提供了 rateLimit 限速、delay 延时入队（由优先级队列通过小顶堆实现）、Queue 队列处理 三大核心能力。<br>
<br>另外，在代码中可看到 Kubernetes 实现了三种 RateLimiter：BucketRateLimiter，ItemExponentialFailureRateLimiter，ItemFastSlowRateLimiter，Controller 默认采用了前两种如下：<br>
<pre class="prettyprint">// staging/src/k8s.io/client-go/util/workqueue/default_rate_limiters.go<br>
func DefaultControllerRateLimiter() RateLimiter &#123;<br>
return NewMaxOfRateLimiter(<br>
NewItemExponentialFailureRateLimiter(5*time.Millisecond, 1000*time.Second),<br>
// 10 qps, 100 bucket size.  This is only for retry speed and its only the overall factor (not per item)<br>
&BucketRateLimiter&#123;Limiter: rate.NewLimiter(rate.Limit(10), 100)&#125;,<br>
)<br>
&#125; <br>
</pre><br>
这样，在用户侧可以通过调用 Workqueue 相关方法进行灵活的队列处理，比如失败多少次就不再重试，失败了延时入队的时间控制，队列的限速控制（QPS）等，实现非阻塞异步化逻辑处理。<br>
<h3>小结</h3>本文通过分析 Kubernetes 中 Reflector（反射器）、DeltaFIFO（增量队列）、Indexer（索引器）、Controller（控制器）、SharedInformer（共享资源通知器）、processorListener（事件监听处理器）、Workqueue（事件处理工作队列）等组件，对 Informer 实现机制进行了解析，通过源码、图文方式说明了相关流程处理，以期更好的理解 Kubernetes Informer 运行流程。<br>
<br>可以看到，Kubernetes 为了实现高效、非阻塞的核心流程，<strong>大量采用了 Goroutine 协程、Channel 通道、Queue 队列、Index 索引、MAP 去重等方式；并通过良好的接口设计模式，给使用者开放了很多扩展能力；采用了统一的接口与实现的命名方式等</strong>，这些都值得深入学习与借鉴。<br>
<br>PS：更多内容请关注 k8s-club GitHub地址：<a href="https://github.com/k8s-club/k8s-club" rel="nofollow" target="_blank">https://github.com/k8s-club/k8s-club</a><br>
<br>参考资料：<br>
<ol><li><a href="https://kubernetes.io/" rel="nofollow" target="_blank">https://kubernetes.io/</a></li><li><a href="https://github.com/kubernetes/kubernetes" rel="nofollow" target="_blank">https://github.com/kubernetes/kubernetes</a></li><li><a href="https://github.com/kubernetes/community/blob/master/contributors/design-proposals/architecture/architectural-roadmap.md" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... ap.md</a></li></ol><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/-qiB1KilhwtcjI61m_x3jA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/-qiB1KilhwtcjI61m_x3jA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            