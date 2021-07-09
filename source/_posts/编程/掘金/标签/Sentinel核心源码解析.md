
---
title: 'Sentinel核心源码解析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35e7b310c1264665958ee071b8ac8f06~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 01:05:30 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35e7b310c1264665958ee071b8ac8f06~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Sentinel：分布式系统的流量防卫兵(防御系统)</h1>
<p>面向分布式服务架构的流量控制组件，主要以流量为切入点，从限流、流量整形、熔断降级、系统负载保护、热点防护等多个维度来帮助开发者保障微服务的稳定性。</p>
<h1 data-id="heading-1">Sentinel工作原理</h1>
<h2 data-id="heading-2">1、架构</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35e7b310c1264665958ee071b8ac8f06~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>ProcessorSlotChain</strong>（核心骨架）：将不同的 Slot 按照顺序串在一起（责任链模式），从而将不同的功能（限流、降级、系统保护）组合在一起。slot chain 其实可以分为两部分：统计数据构建部分（statistic）和判断部分（rule checking）。
<strong>系统会为每个资源创建一套SlotChain</strong>。</p>
<h2 data-id="heading-3">2、SPI机制</h2>
<p>Sentinel槽链中Slot执行顺序是固定的，但并不是绝对的。Sentinel将ProcessorSlot作为SPI接口进行扩展，使得SlotChain具备了扩展能力。用户可以自定义Slot并编排Slot间的顺序。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b492ffa8006147ff95b3074caa339192~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>代码实现</strong></p>
<p>继承AbstractLinkedProcessorSlot，并设置@Spi(order)</p>
<pre><code class="copyable">@Spi(order = Constants.ORDER_FLOW_SLOT)
public class FlowSlot extends AbstractLinkedProcessorSlot<DefaultNode> &#123;
    ... ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">3、slot</h2>
<blockquote>
<p><strong>工作流程</strong>： Sentinel工作主流程就包含在SphU.entry方法里，通过链式调用的方式，经过了建立树状结构，保存统计簇点，异常日志记录，实时数据统计，负载保护，权限认证，流量控制，熔断降级等Slot</p>
</blockquote>
<p><strong>调用链</strong>：</p>
<blockquote>
<p>META-INF/services/com.alibaba.csp.sentinel.slotchain.ProcessorSlot</p>
</blockquote>
<p><strong>NodeSelectorSlot</strong> >>> ClusterBuilderSlot >>> <em>LogSlot</em> >>> <strong>StatisticSlot</strong> >>> ParamFlowSlot >>> SystemSlot >>> AuthoritySlot >>> <strong>FlowSlot</strong> >>> <strong>DegradeSlot</strong></p>
<ul>
<li><strong>NodeSelectorSlot</strong> 负责收集资源的路径，并将这些资源的调用路径，以树状结构存储起来，用于根据调用路径来限流降级；</li>
<li><strong>ClusterBuilderSlot</strong> 则用于存储资源的统计信息以及调用者信息，例如该资源的 RT, QPS, thread count 等等，这些信息将用作为多维度限流，降级的依据；</li>
<li><strong>StatisticSlot</strong> 则用于记录、统计不同纬度的 runtime 指标监控信息；</li>
<li><strong><em>ParamFlowSlot</em>（热点流控）</strong> 对应热点流控（针对资源的热点参数做流量控制）</li>
<li><strong>SystemSlot（系统规则）</strong> 则通过系统的状态，例如 load1 等，来控制总的入口流量；（针对当前服务做全局流量控制）</li>
<li><strong>AuthoritySlot（授权规则）</strong> 则根据配置的黑白名单和调用来源信息，来做黑白名单控制；（对访问资源的特定应用做授权处理）</li>
<li><strong>FlowSlot（流控规则）</strong> 则用于根据预设的限流规则以及前面 slot 统计的状态，来进行流量控制；（针对资源流量控制）</li>
<li><strong>DegradeSlot（降级规则）</strong> 则通过统计信息以及预设的规则，来做熔断降级；（针对资源的调度情况来做降级处理）</li>
</ul>
<h2 data-id="heading-5">4、Node</h2>
<p><strong>树形结构</strong>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8947bdad89f44926bf448e822136c235~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>类关系</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be79accdcd714695909ce9e01d50e473~tplv-k3u1fbpfcp-watermark.image" alt="企业微信截图_4ebb787c-bdde-4884-8586-f420d5f12836.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>Entry（资源）</strong>：包含了资源名、curNode（当前统计节点）、originNode（来源统计节点）等信息。构造函数中会做调用链的变换，即将当前 Entry 接到传入 Context 的调用链路上。</p>
</blockquote>
<blockquote>
<p><strong>Context（资源操作上下文）</strong>：每个资源操作必须属于一个Context（通过ThreadLocal 传递）。若未指定，会创建默认name=sentinel_default_context。一个Context生命周期中可以包含多个
资源操作。Context生命周期中的最后一个资源在exit()时会清理该Conetxt，意味着这个Context生命周期结束。</p>
</blockquote>















































<table><thead><tr><th>节点</th><th>说明</th><th>维度</th><th>创建时机</th><th>备注</th></tr></thead><tbody><tr><td><strong>ROOT</strong></td><td>invocation tree（调用树）根</td><td>一个应用创建一个</td><td>系统启动</td><td></td></tr><tr><td><strong>EntranceNode</strong></td><td>入口节点，某个Context（一次请求）入口的所有调用数据</td><td>context</td><td>ContextUtil.enter</td><td>context</td></tr><tr><td><strong>DefaultNode</strong></td><td>链路节点，用于统计调用链路上某个资源的数据</td><td>resource * context</td><td>NodeSelectorSlot根据context创建</td><td>set curNode to context</td></tr><tr><td><strong>ClusterNode</strong></td><td>簇点，用于统计每个资源全局的数据</td><td>resource</td><td>ClusterBuilderSlot根据resourceName创建</td><td>set clusterNode to defaultNode</td></tr><tr><td><strong>StatisticNode</strong></td><td>统计节点，包含秒/分钟级滑动窗口</td><td>resource * origin</td><td>来源节点根据origin创建</td><td>set originNode to curEntry</td></tr></tbody></table>
<h1 data-id="heading-6">核心源码</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5336bc8dbd14f559f58913f58a9fbce~tplv-k3u1fbpfcp-watermark.image" alt="sentinel客户端.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Sentinel每种资源（Entry）有一个独有的Slot Chain，一起实现整体的流量控制。 </p>
<p><strong>核心类</strong>：</p>
<ul>
<li><strong>SphU</strong> - Sentinel静态调用入口</li>
<li><strong>CtSph</strong> - 实际调用入口</li>
<li><strong>Context</strong> - 资源上下文，同一个资源可以包含在不同的context中</li>
<li><strong>CtEntry</strong> - 代表实际资源</li>
<li><strong>DefaultProcessorSlotChain</strong> - slot chain默认实现</li>
<li><strong>ProcessorSlot及子类</strong> - 不同的slot实现</li>
</ul>
</blockquote>
<h2 data-id="heading-7">1、SentinelResourceAspect - 入口</h2>
<p>Spring AOP：AspectJ 切入点 （<strong>以注解方式为例</strong>）</p>
<pre><code class="copyable">@Aspect
public class SentinelResourceAspect extends AbstractSentinelAspectSupport &#123;
    // 切入点为：@SentinelResource 
    @Pointcut("@annotation(com.alibaba.csp.sentinel.annotation.SentinelResource)")
    public void sentinelResourceAnnotationPointcut() &#123;
    &#125;
    // 环绕通知
    @Around("sentinelResourceAnnotationPointcut()")
    public Object invokeResourceWithSentinel(ProceedingJoinPoint pjp) throws Throwable &#123;
        ... ...
        String resourceName = getResourceName(annotation.value(), originMethod);
        EntryType entryType = annotation.entryType();
        int resourceType = annotation.resourceType();
        Entry entry = null;
        try &#123;
            // 【资源：工作主流程】要织入的、增强的功能
            entry = SphU.entry(resourceName, resourceType, entryType, pjp.getArgs());
            // 调用目标方法
            return pjp.proceed();
        &#125; catch (BlockException ex) &#123;
            return handleBlockException(pjp, annotation, ex);
        &#125; catch (Throwable ex) &#123;
            // No fallback function can handle the exception, so throw it out.
            throw ex;
        &#125; finally &#123;
            if (entry != null) &#123;
                // 当前资源增强功能处理结束
                entry.exit(1, pjp.getArgs());
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">2、调用入口</h2>
<h3 data-id="heading-9">2.1、SphU - 静态调用入口</h3>
<p>主要做了五件事</p>
<ul>
<li>1、将资源名称和流量类型进行包装</li>
<li>2、从当前线程得到context，如果之前没有创建context，则这里会创建一个context-name为sentinel_default_name、original为""的context</li>
<li>3、添加一个规则检查调用链，根据我们配置的规则一层一层进行检查，只要在某一个规则未通过就提前结束抛出该规则对应的异常</li>
<li>4、创建一个流量入口entry，它用来保存本次调用的信息，将context的curEntry进行指定</li>
<li>5、开始执行规则检查调用链</li>
</ul>
<pre><code class="copyable">public static Entry entry(String name, int resourceType, EntryType trafficType, Object[] args)
        throws BlockException &#123;
        // name:资源名， resourceType:资源类型，entryType:流量类型为入口还是出口（系统规则只针对入口流量），args:参数，后面做热点参数规则时用到
        // batchCount：默认1个请求
        return Env.sph.entryWithType(name, resourceType, trafficType, 1, args);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2.2、CtSph - 实际调用入口</h3>
<pre><code class="copyable">private Entry entryWithPriority(ResourceWrapper resourceWrapper, int count, boolean prioritized, Object... args)
        throws BlockException &#123;
        // 【关注点】当前线程持有的context（ThreadLocal）：一个请求占用一个线程、一个线程绑定一个context
        Context context = ContextUtil.getContext();
        if (context instanceof NullContext) &#123;
            // 当前系统中的context数量（请求数量）超出阈值：直接返回一个无需校验规则的资源对象
            return new CtEntry(resourceWrapper, null, context);
        &#125;

        if (context == null) &#123;
            // 创建默认名称（sentinel_default_context）：放入ThreadLocal
            context = InternalContextUtil.internalEnter(Constants.CONTEXT_DEFAULT_NAME);
        &#125;

        // 全局开关-关闭：不进行规则检查，直接返回一个无需校验规则的资源对象
        if (!Constants.ON) &#123;
            return new CtEntry(resourceWrapper, null, context);
        &#125;

        // 添加一个规则检查调用链
        ProcessorSlot<Object> chain = lookProcessChain(resourceWrapper);

        // 未找到chain（意味chain数量超出阈值）：直接返回一个无需校验规则的资源对象
        if (chain == null) &#123;
            return new CtEntry(resourceWrapper, null, context);
        &#125;

        // 创建一个资源对象：一个流量入口,将context curEntry进行指定
        Entry e = new CtEntry(resourceWrapper, chain, context);
        try &#123;
            // 开始规则检查
            chain.entry(context, resourceWrapper, null, count, prioritized, args);
        &#125; catch (BlockException e1) &#123;
            // 发生流控异常进行退出
            e.exit(count, args);
            // 将异常向上抛
            throw e1;
        &#125; catch (Throwable e1) &#123;
            RecordLog.info("Sentinel unexpected exception", e1);
        &#125;
        return e;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">3、Context - 资源上下文</h2>
<p>同一个资源可以包含在不同的context中：统计资源的调用信息，如QPS、rt等信息</p>
<pre><code class="copyable">protected static Context trueEnter(String name, String origin) &#123;
    // 尝试：从当前线程上下文（ThreadLocal）中拿
    Context context = contextHolder.get();
    if (context == null) &#123;
        // 尝试：从缓存map的key=context-name，value=EntranceNode
        Map<String, DefaultNode> localCacheNameMap = contextNameNodeMap;
        // 获取EntranceNode：context-name对应的DefaultNode
        DefaultNode node = localCacheNameMap.get(name);
        if (node == null) &#123;
            // 限制2000，也就是最多申明2000不同名称的上下文
            if (localCacheNameMap.size() > Constants.MAX_CONTEXT_NAME_SIZE) &#123;
                setNullContext();
                return NULL_CONTEXT;
            &#125; else &#123;
                LOCK.lock();
                try &#123;
                    // 防止并发，再次检查
                    node = contextNameNodeMap.get(name);
                    if (node == null) &#123;
                        if (contextNameNodeMap.size() > Constants.MAX_CONTEXT_NAME_SIZE) &#123;
                            setNullContext();
                            return NULL_CONTEXT;
                        &#125; else &#123;
                            // 创建EntranceNode
                            node = new EntranceNode(new StringResourceWrapper(name, EntryType.IN), null);
                            // Add entrance node. 将新建的node添加到ROOT
                            Constants.ROOT.addChild(node);

                            // 将新建node写入缓存map
                            // 为了"防止迭代稳定性问题"：iterate stable （对于共享集合的写操作：否则可能引发读操作读到脏数据）
                            Map<String, DefaultNode> newMap = new HashMap<>(contextNameNodeMap.size() + 1);
                            newMap.putAll(contextNameNodeMap);
                            newMap.put(name, node);
                            contextNameNodeMap = newMap;
                        &#125;
                    &#125;
                &#125; finally &#123;
                    LOCK.unlock();
                &#125;
            &#125;
        &#125;
        // 将context-name与EntranceNode封装为context
        context = new Context(node, name);
        // 初始化context来源
        context.setOrigin(origin);
        // 将context写入ThreadLocal
        contextHolder.set(context);
    &#125;

    return context;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">4、DefaultProcessorSlotChain - slot chain默认实现</h2>
<p>单向链表：默认创建一个节点，且两个指针（first、end）同时指向该节点</p>
<pre><code class="copyable">AbstractLinkedProcessorSlot<?> first = new AbstractLinkedProcessorSlot<Object>() &#123;
    @Override
    public void entry(Context context, ResourceWrapper resourceWrapper, Object t, int count, boolean prioritized, Object... args)
        throws Throwable &#123;
        super.fireEntry(context, resourceWrapper, t, count, prioritized, args);
    &#125;

    @Override
    public void exit(Context context, ResourceWrapper resourceWrapper, int count, Object... args) &#123;
        super.fireExit(context, resourceWrapper, count, args);
    &#125;

&#125;;
AbstractLinkedProcessorSlot<?> end = first;
    
@Override
public void entry(Context context, ResourceWrapper resourceWrapper, Object t, int count, boolean prioritized, Object... args)
        throws Throwable &#123;
    // 转换操作对象：从first节点转向下一个节点
    first.transformEntry(context, resourceWrapper, t, count, prioritized, args);
&#125;

@Override
public void addLast(AbstractLinkedProcessorSlot<?> protocolProcessor) &#123;
    // end节点下一个节点：指定新的节点
    end.setNext(protocolProcessor);
    // end节点：设为新的节点
    end = protocolProcessor;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">5、ProcessorSlot及子类 - 不同的slot实现</h2>
<blockquote>
<p>META-INF/services/com.alibaba.csp.sentinel.slotchain.ProcessorSlot</p>
</blockquote>
<p>获取SlotChain：按顺序挨个判断</p>
<pre><code class="copyable">// CtSph
ProcessorSlot<Object> lookProcessChain(ResourceWrapper resourceWrapper) &#123;
        // 从缓存：获取当前资源的SlotChain（key=资源，value=其相关ProcessorSlotChain）
        ProcessorSlotChain chain = chainMap.get(resourceWrapper);
        if (chain == null) &#123;
            // 缓存无：创建并放入缓存
            synchronized (LOCK) &#123;
                chain = chainMap.get(resourceWrapper);
                if (chain == null) &#123;
                    // Entry// 创建新的chain size limit.
                    // 缓存map的size >= chain数量最大阈值，直接返回null
                    if (chainMap.size() >= Constants.MAX_SLOT_CHAIN_SIZE) &#123;
                        return null;
                    &#125;

                    // 【重点】创建新的chain
                    chain = SlotChainProvider.newSlotChain();

                    // 防止迭代稳定性问题
                    Map<ResourceWrapper, ProcessorSlotChain> newMap = new HashMap<ResourceWrapper, ProcessorSlotChain>(
                        chainMap.size() + 1);
                    newMap.putAll(chainMap);
                    newMap.put(resourceWrapper, chain);
                    chainMap = newMap;
                &#125;
            &#125;
        &#125;
        return chain;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">5.1、NodeSelectorSlot</h3>
<p>负责收集资源的路径，并将这些资源的调用路径，以树状结构存储起来，用于根据调用路径来限流降级</p>
<p>根据 context 创建 DefaultNode。</p>
<pre><code class="copyable">@Override
public void entry(Context context, ResourceWrapper resourceWrapper, Object obj, int count, boolean prioritized, Object... args)
    throws Throwable &#123;
    // 从缓存中获取DefaultNode
    DefaultNode node = map.get(context.getName());
    if (node == null) &#123;
        synchronized (this) &#123;
            node = map.get(context.getName());
            if (node == null) &#123;
                // 创建DefaultNode
                node = new DefaultNode(resourceWrapper, null);
                HashMap<String, DefaultNode> cacheMap = new HashMap<String, DefaultNode>(map.size());
                cacheMap.putAll(map);
                cacheMap.put(context.getName(), node);
                map = cacheMap;
                // Build invocation tree
                // 将新建node添加到调用树
                ((DefaultNode) context.getLastNode()).addChild(node);
            &#125;

        &#125;
    &#125;

    context.setCurNode(node);
    // 【关注点】触发下一个节点
    fireEntry(context, resourceWrapper, node, count, prioritized, args);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">5.2、StatisticSlot</h3>
<p>记录、统计不同纬度的 runtime 指标监控信息；</p>
<p>注意：先调用SlotChain中后续的所有Slot，完成所有规则检测。然后再统计。</p>
<pre><code class="copyable">@Override
public void entry(Context context, ResourceWrapper resourceWrapper, DefaultNode node, int count,
                      boolean prioritized, Object... args) throws Throwable &#123;
    try &#123;
        // 向后传递：调用SlotChain中后续的所有Slot，完成所有规则检测（执行过程中可能回抛出异常：如，BlockException）
        fireEntry(context, resourceWrapper, node, count, prioritized, args);

        // 前面所有规则检测通过：对DefaultNode添加线程数和qps（通过的请求数量：涉及滑动窗口）
        node.increaseThreadNum();
        node.addPassRequest(count);

       ... ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">5.3、FlowSlot</h3>
<p>根据预设的限流规则以及前面 slot 统计的状态，来进行流量控制；</p>
<pre><code class="copyable">@Override
public boolean canPass(Node node, int acquireCount, boolean prioritized) &#123;
    // 获取当前时间窗已统计数据：node的ThreadNum或QPS
    int curCount = avgUsedTokens(node);
    if (curCount + acquireCount > count) &#123;
        // 设置当前流量为优先级和流控模式为QPS（prioritized=true）：要等待
        if (prioritized && grade == RuleConstant.FLOW_GRADE_QPS) &#123;
            long currentTime;
            long waitInMs;
            currentTime = TimeUtil.currentTimeMillis();
            // 算出拿到当前令牌数的等待时间(ms)
            waitInMs = node.tryOccupyNext(currentTime, acquireCount, count);
            // OccupyTimeoutProperty.getOccupyTimeout = 500ms
            // 如果流量具有优先级，会获取未来的令牌数
            if (waitInMs < OccupyTimeoutProperty.getOccupyTimeout()) &#123;
                // 添加占用未来的QPS，会调用OccupiableBucketLeapArray.addWaiting(long time, int acquireCount)
                node.addWaitingRequest(currentTime + waitInMs, acquireCount);
                node.addOccupiedPass(acquireCount);
                sleep(waitInMs);

                throw new PriorityWaitException(waitInMs);
            &#125;
        &#125;
        return false;
    &#125;
    return true;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">5.5、DegradeSlot</h3>
<p>通过统计信息以及预设的规则，来做熔断降级；</p>
<p>注意：只看到了状态从OPEN变为HALF_OPEN，HALF_OPEN变为OPEN，但没有看到状态如何从HALF_OPEN变为CLOSE的，它的变化过程是在正常执行完请求后,entry.exit()会调用DegradeSlot.exit()方法来改变状态</p>
<pre><code class="copyable">@Override
public boolean tryPass(Context context) &#123;
    // Template implementation.
    // 正常通行
    if (currentState.get() == State.CLOSED) &#123;
        return true;
    &#125;
    // 尝试通行
    if (currentState.get() == State.OPEN) &#123;
        // For half-open state we allow a request for probing.
        // 下次时间窗时间点到了，且 open变为halfOpen （【注意】halfOpen：只能由系统从open转为）
        return retryTimeoutArrived() && fromOpenToHalfOpen(context);
    &#125;
    return false;
&#125;

protected boolean fromOpenToHalfOpen(Context context) &#123;
    // 尝试将状态从OPEN设置为HALF_OPEN
    if (currentState.compareAndSet(State.OPEN, State.HALF_OPEN)) &#123;
        // 状态变化通知
        notifyObservers(State.OPEN, State.HALF_OPEN, null);
        Entry entry = context.getCurEntry();
        // 在entry添加一个exitHandler entry.exit()时会调用
        entry.whenTerminate(new BiConsumer<Context, Entry>() &#123;
            @Override
            public void accept(Context context, Entry entry) &#123;
                // 如果有发生异常，重新将状态设置为OPEN 请求不同通过
                if (entry.getBlockError() != null) &#123;
                    // Fallback to OPEN due to detecting request is blocked
                    currentState.compareAndSet(State.HALF_OPEN, State.OPEN);
                    notifyObservers(State.HALF_OPEN, State.OPEN, 1.0d);
                &#125;
            &#125;
        &#125;);
        return true;
    &#125;
    return false;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">6、Sentinel Dashboard服务端源码</h2>
<p><strong>主要做三件事</strong></p>
<ul>
<li>使用spi加载com.alibaba.csp.sentinel.init.InitFunc的一些实现类；</li>
<li>将加载后的实现类进行排序；</li>
<li>调用这些实现类的初始化方法
<ol>
<li>CommandCenterInitFunc：获取命令中心，做一些准备工作（注册dashboard接口处理器），然后创建一个socket监听8719端口(sentinel与客户端通信的端口号)</li>
<li>HeartbeatSenderInitFunc：心跳相关任务初始化</li>
<li>MetricCallbackInit：注册扩展的入口和出口回调类</li>
<li>ParamFlowStatisticSlotCallbackInit：注册参数流入口和出口回调类</li>
</ol>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/548978068eb84f11a118f080b59c77f7~tplv-k3u1fbpfcp-watermark.image" alt="Sentinel服务端.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-19">参考资料</h5>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2FSentinel%2Fwiki%2FSentinel%25E5%25B7%25A5%25E4%25BD%259C%25E4%25B8%25BB%25E6%25B5%2581%25E7%25A8%258B" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/Sentinel/wiki/Sentinel%E5%B7%A5%E4%BD%9C%E4%B8%BB%E6%B5%81%E7%A8%8B" ref="nofollow noopener noreferrer">官方文档</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2Fsentinel%2Fwiki%2Fsentinel-%25E6%25A0%25B8%25E5%25BF%2583%25E7%25B1%25BB%25E8%25A7%25A3%25E6%259E%2590" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/sentinel/wiki/sentinel-%E6%A0%B8%E5%BF%83%E7%B1%BB%E8%A7%A3%E6%9E%90" ref="nofollow noopener noreferrer">Sentinel 核心类解析</a></p></div>  
</div>
            