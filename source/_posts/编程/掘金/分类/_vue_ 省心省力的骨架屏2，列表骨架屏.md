
---
title: '_vue_ 省心省力的骨架屏2，列表骨架屏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2025d0a05af841b2b7ab718a5703699b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 20:20:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2025d0a05af841b2b7ab718a5703699b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">vue3 骨架屏+上拉加载更多封装</h1>
<h2 data-id="heading-1">前言,介绍</h2>
<p>这个列表的骨架屏之前有个初代的版本，也写过一次博客，不过是发在了csdn上面，后来改了一次，因为那篇博文阅读量不高，也没动力去更了。初代版本跟现在主要区别是实现思路不一样，之前是使用骨架屏是一个模块，然后具体列表渲染又是一个模块，切换的时候是整个来切的，过渡虽然有，但是不是特别自然，这个第二版就是采用的和我之前的博文<a href="https://juejin.cn/post/6945748911147450405" target="_blank">一个省心省力的骨架屏</a>一样的方案了，都是替换css。写法上也有不同，这次参考了 有赞 团队的 <a href="https://vant-contrib.gitee.io/vant/v3/#/zh-CN/list" target="_blank" rel="nofollow noopener noreferrer">vant</a> 的list写法(抄了好多代码)，相当于在 vant的list组件上加了骨架屏功能了，感谢vant团队。</p>
<h3 data-id="heading-2">功能</h3>
<p>提供骨架屏展示、瀑布流滚动加载，用于展示长列表，当列表即将滚动到底部时，会触发事件并加载更多列表项。</p>
<h3 data-id="heading-3">效果（选择网点时）</h3>
<p><img alt="效果" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2025d0a05af841b2b7ab718a5703699b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">用法</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"router_view"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"height:800px;overflow-y: auto;"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ListView</span> 
        <span class="hljs-attr">:list-data</span>=<span class="hljs-string">"data"</span>  
        <span class="hljs-attr">:bind-scroll-document</span>=<span class="hljs-string">"routerView"</span> 
        <span class="hljs-attr">:empty-item</span>=<span class="hljs-string">"emptyItem"</span> 
        <span class="hljs-attr">:finished</span>=<span class="hljs-string">"finished"</span>
        <span class="hljs-attr">v-model:loading</span>=<span class="hljs-string">"showLoading"</span>
        <span class="hljs-attr">:error</span>=<span class="hljs-string">"showError"</span>
        @<span class="hljs-attr">load</span>=<span class="hljs-string">"requestData"</span>
        <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; item &#125;"</span>
        ></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item row-center item-between"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">img</span>
                    <span class="hljs-attr">class</span>=<span class="hljs-string">"item_pic"</span>
                    <span class="hljs-attr">:src</span>=<span class="hljs-string">"item.full_photo"</span>
                /></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"col center_info"</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>
                    联系人: &#123;&#123; item.concact_name &#125;&#125;
                    <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"time"</span>></span>
                    填写时间: &#123;&#123; item.collection_time &#125;&#125;
                   <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">router-link</span>
                 <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; path: '/form', 
                 query: &#123; mode: 'edit_draft',fileId:item.fileid &#125;&#125;"</span>
                 <span class="hljs-attr">class</span>=<span class="hljs-string">"edit_text"</span> 
                 ></span>编辑</router-link
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ListView</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><script lang=<span class="hljs-string">'ts'</span>>
<span class="hljs-keyword">import</span> &#123; defineComponent, reactive, toRefs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> ListView <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/list_view/list_view.vue"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">components</span>: &#123;
    ListView,
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> state = reactive(&#123;
      <span class="hljs-attr">list</span>: [],
      <span class="hljs-attr">showLoading</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">showError</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">finished</span>: <span class="hljs-literal">false</span>
    &#125;);

<span class="hljs-comment">// 设置骨架屏所用到的数据模板，主要用于撑开span标签</span>
    <span class="hljs-keyword">const</span> emptyItem = &#123;
      <span class="hljs-attr">full_photo</span>: <span class="hljs-string">""</span>,
      <span class="hljs-attr">concact_name</span>: <span class="hljs-string">"asdasd"</span>,
      <span class="hljs-attr">collection_time</span>: <span class="hljs-string">"2021-3-3 15:23"</span>,
    &#125;;
    
<span class="hljs-comment">//绑定一个可滑动的容器，默认情况下是window，也就是浏览器的默认滑动</span>
<span class="hljs-comment">// 如果限定列表是在某一个元素内滑动，就需要把这个可滑动的元素传入ListView组件</span>
<span class="hljs-comment">// 用来绑定滑动事件，如果没有不传就好了</span>
    <span class="hljs-keyword">const</span> routerView = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".router_view"</span>);

    <span class="hljs-keyword">const</span> requestData = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 异步更新数据</span>
      <span class="hljs-comment">// setTimeout 仅做示例，真实场景中一般为 ajax 请求</span>
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
          state.list.push(&#123;
<span class="hljs-attr">full_photo</span>:<span class="hljs-string">"http://static.feidaojixie.com/machine/51271/full_photo/e9532332299e357ab815373a145f8ce2"</span>,
            <span class="hljs-attr">concact_name</span>: <span class="hljs-string">"联系人"</span> + (state.list.length + <span class="hljs-number">1</span>),
            <span class="hljs-attr">collection_time</span>: <span class="hljs-string">"2021-3-3 15:23"</span>,
          &#125;);
        &#125;
        <span class="hljs-comment">// 加载状态结束</span>
        state.showLoading = <span class="hljs-literal">false</span>;

        <span class="hljs-comment">// 数据全部加载完成</span>
        <span class="hljs-keyword">if</span> (state.list.length >= <span class="hljs-number">40</span>) &#123;
          state.finished = <span class="hljs-literal">true</span>;
        &#125;
      &#125;, <span class="hljs-number">3000</span>);
    &#125;;
    <span class="hljs-keyword">return</span> &#123;
      ...toRefs(state),
      emptyItem,
      routerView,
      requestData,
    &#125;;
  &#125;,
&#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>API
<ul>
<li>Props</li>
</ul>
</li>
</ul>

























































































<table><thead><tr><th>参数</th><th>说明</th><th>类型</th><th>默认值</th></tr></thead><tbody><tr><td>list-data</td><td>数据数组</td><td>Array</td><td>[]</td></tr><tr><td>bind-key</td><td>vue的for循环绑定的key</td><td>String,Function</td><td>默认值为index</td></tr><tr><td>v-model:loading</td><td>是否处于加载状态，加载过程中不触发 load 事件</td><td>Boolean</td><td>false</td></tr><tr><td>error</td><td>是否加载失败，加载失败后点击错误提示可</td><td></td><td></td></tr><tr><td>以重新触发 load 事件</td><td>boolean</td><td>false</td><td></td></tr><tr><td>finished</td><td>是否已加载完成，加载完成后不再触发 load 事件</td><td>Boolean</td><td>false</td></tr><tr><td>loading-text</td><td>加载过程中的提示文案</td><td>String</td><td>加载中...</td></tr><tr><td>finished-text</td><td>加载完成后的提示文案</td><td>String</td><td>没有更多了...</td></tr><tr><td>error-text</td><td>加载失败后的提示文案</td><td>String</td><td>加载失败了，点我重新加载</td></tr><tr><td>empty-text</td><td>数据为空时的提示文案</td><td>String</td><td>暂无数据</td></tr><tr><td>immediate-check</td><td>是否在初始化时立即执行滚动位置检查</td><td>Boolean</td><td>true</td></tr><tr><td>empty-item</td><td>设置骨架屏所用到的数据模板，主要用于撑开元素标签</td><td>Object</td><td>&#123;&#125;</td></tr><tr><td>bind-scroll-document</td><td>列表所在的可滑动的容器，默认为window</td><td>Object</td><td>window</td></tr></tbody></table>
<ul>
<li>Events</li>
</ul>















<table><thead><tr><th align="left">事件名</th><th align="left">说明</th><th align="left">回调参数</th></tr></thead><tbody><tr><td align="left">load</td><td align="left">滚动条与底部距离小于 offset 时触发</td><td align="left">-</td></tr></tbody></table>
<ul>
<li>Slots</li>
</ul>





























<table><thead><tr><th align="left">名称</th><th align="left">说明</th></tr></thead><tbody><tr><td align="left">default</td><td align="left">列表内容</td></tr><tr><td align="left">loading</td><td align="left">自定义底部加载中提示</td></tr><tr><td align="left">finished</td><td align="left">自定义底部加载完成提示</td></tr><tr><td align="left">error</td><td align="left">自定义底部加载失败提示</td></tr><tr><td align="left">empty</td><td align="left">自定义列表数据为空提示</td></tr></tbody></table>
<h3 data-id="heading-5">问题</h3>
<ul>
<li>
<p>骨架屏使用什么实现？
骨架屏是通过css样式给子项中的img和span、a标签设置背景色来实现的，所以需要传递 empty-item 参数来撑起列表元素的span和a标签，如果你还使用了其他标签，可以参考源码中css样式添加其他标签</p>
</li>
<li>
<p>List 的运行机制是什么？
List 会监听浏览器或目标元素的滚动事件并计算列表的位置，当列表底部与可视区域的距离小于 offset 时，List 会触发一次 load 事件。</p>
</li>
<li>
<p>loading 和 finished 分别是什么含义？
List 有以下五种状态，理解这些状态有助于你正确地使用 List 组件：</p>
<ol>
<li>init，初始化加载中，当loading为true且listData长度为0时，为init状态，此时显示骨架屏</li>
<li>非加载中，loading 为 false，此时会根据列表滚动位置判断是否触发 load 事件</li>
<li>加载中，loading 为 true，表示正在发送异步请求，此时不会触发 load 事件</li>
<li>加载完成，finished 为 true且listData长度不为0，此时不会触发 load 事件</li>
<li>暂无数据，finished为true，loading为false，finished 为true</li>
</ol>
<p>在每次请求完毕后，需要手动将 loading 设置为 false，表示加载结束</p>
</li>
</ul>
<h3 data-id="heading-6">全部代码</h3>
<blockquote>
<p>如果你觉着复制代码太麻烦，可以直接使用我的模板，里面有全部代码，下次我们再讲这个模板</p>
</blockquote>
<pre><code class="copyable">// 使用yarn构建
vue create --preset direct:https://gitee.com/wqja/vue3_ts_preset.git --clone my-project
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>ListView.tsx</li>
</ul>
<pre><code class="hljs language-tsx copyable" lang="tsx">import &#123;computed, defineComponent, nextTick, onMounted, onUpdated, PropType, ref, watch&#125; from 'vue';
import './list_view.css'
import './skeleton.css'

// 这里直接使用了vant的工具类
import &#123; useRect, useScrollParent, useEventListener &#125; from '@/use';
import &#123;isHidden&#125; from "@/util/Utils";

type ViewStatusType = 'INIT'|'SHOW'|'ERROR'|'FINISHED'|'EMPTY';

export default defineComponent(&#123;
    name:'ListViewTSX',
    props:&#123;
        listData: &#123;
            type: Array,
            default: () => &#123;
                return [];
            &#125;,
        &#125;,
        bindKey:&#123;
            type: [String,Function],
            default:() => null
        &#125;,
        loading: &#123;
            type: Boolean,
            default: () => false,
        &#125;,
        error: &#123;
            type: Boolean,
            default: () => false,
        &#125;,
        finished: &#123;
            type: Boolean,
            default: () => false,
        &#125;,
        emptyText: &#123;
            type: String,
            default: () => &#123;
                return "暂无数据";
            &#125;,
        &#125;,
        emptyItem: &#123;
            type: Object,
            default: () => &#123;
                return &#123;&#125;;
            &#125;
        &#125;,
        placeCount:&#123;
            type: Number,
            default: () => &#123;
                return 10;
            &#125;
        &#125;,
        loadingText: &#123;
            type: String,
            default: () => "加载中...",
        &#125;,
        finishedText: &#123;
            type: String,
            default: () => "没有更多了",
        &#125;,
        errorText: &#123;
            type: String,
            default: () => "加载失败了，点我重新加载",
        &#125;,
        offset: &#123;
            type: Number,
            default: () => 100,
        &#125;,
        immediateCheck: &#123;
            type: Boolean,
            default: () => true,
        &#125;,
        direction: &#123;
            type: String as PropType<'up' | 'down'>,
            default: 'down',
        &#125;,
        noPackage:&#123;
            type: Boolean,
            default:()=>&#123;
                return false;
            &#125;
        &#125;
    &#125;,
    emits: ['load', 'update:error', 'update:loading'],
    setup(props,&#123; emit, slots &#125;) &#123;

        const loading = ref(false);
        const root = ref<HTMLElement>();
        const placeholder = ref<HTMLElement>();
        const scrollParent = useScrollParent(root);

        const check = () => &#123;
            nextTick(() => &#123;
                if (loading.value || props.finished || props.error) &#123;
                    return;
                &#125;

                const &#123; offset,direction &#125; = props;
                const scrollParentRect = useRect(scrollParent);

                if (!scrollParentRect.height || isHidden(root)) &#123;
                    return false;
                &#125;

                let isReachEdge = false;
                const placeholderRect = useRect(placeholder);

                if (direction === 'up') &#123;
                    isReachEdge = scrollParentRect.top - placeholderRect.top <= offset;
                &#125; else &#123;
                    isReachEdge =
                        placeholderRect.bottom - scrollParentRect.bottom <= offset;
                &#125;

                if (isReachEdge) &#123;
                    loading.value = true;
                    emit('update:loading', true);
                    emit('load');
                &#125;
            &#125;);
        &#125;;

        watch([() => props.loading, () => props.finished], check);

        onUpdated(() => &#123;
            loading.value = props.loading!;
        &#125;);

        onMounted(() => &#123;
            if (props.immediateCheck) &#123;
                check();
            &#125;
        &#125;);

        useEventListener('scroll', check, &#123; target: scrollParent &#125;);



        const clickErrorText = () => &#123;
            emit('update:error', false);
            check();
        &#125;;



        const viewStatus = computed<ViewStatusType>(():ViewStatusType => &#123;
            if (props.listData.length === 0 && props.loading) &#123;
                return "INIT";
            &#125;
            if (props.listData.length === 0 && props.finished) &#123;
                return "EMPTY";
            &#125;
            if (props.error) &#123;
                return "ERROR";
            &#125;
            if (props.finished) &#123;
                return "FINISHED";
            &#125;
            return "SHOW";
        &#125;);

        const listData = computed(()=>&#123;
            if(viewStatus.value==='INIT')&#123;
                const emptyArr = [];
                const count = props.placeCount>10?10:props.placeCount;
                for(let i=0;i<count;i++)&#123;
                    emptyArr.push(props.emptyItem);
                &#125;
                return emptyArr;
            &#125;else if(viewStatus.value === 'EMPTY')&#123;
                return []
            &#125;
            return props.listData;
        &#125;)


        const itemKeyFun = (item,index):string => &#123;
            if(viewStatus.value==='INIT')&#123;
                return index;
            &#125;
            if(!props.bindKey)&#123;
                return index;
            &#125;else&#123;
                if(props.bindKey instanceof Function)&#123;
                    return props.bindKey(item,index);
                &#125;else&#123;
                    return item[props.bindKey]
                &#125;
            &#125;
        &#125;


        const contentList = () =>&#123;
            if(props.noPackage)&#123;
                return listData.value.map((e,index)=>&#123;
                    return slots.default?.(&#123;
                            item:e,
                            index:index,
                            vClass:viewStatus.value==='INIT'?'skeleton-view-empty-view':'skeleton-view-default-view'
                        &#125;)
                &#125;)
            &#125;else&#123;
                return listData.value.map((e,index)=>&#123;
                    return (
                        <div key=&#123;itemKeyFun(e,index)&#125; class=&#123;viewStatus.value==='INIT'?'skeleton-view-empty-view':'skeleton-view-default-view'&#125;>&#123;
                            slots.default?.(&#123;
                                item:e,
                                index:index
                            &#125;)&#125;
                        </div>
                    )
                &#125;)
            &#125;
        &#125;

        const renderFinishedText = () => &#123;
            if (viewStatus.value === 'FINISHED') &#123;
                const text = slots.finished ? slots.finished() : props.finishedText;
                if (text) &#123;
                    return <div class='list-view-center'>&#123;text&#125;</div>;
                &#125;
            &#125;
        &#125;;

        const renderErrorText = () => &#123;
            if (viewStatus.value === 'ERROR') &#123;
                const text = slots.error ? slots.error() : props.errorText;
                if (text) &#123;
                    return (
                        <div class='list-view-center' onClick=&#123;clickErrorText&#125;>
                            &#123;text&#125;
                        </div>
                    );
                &#125;
            &#125;
        &#125;;

        const renderLoading = () => &#123;
            if (viewStatus.value === 'SHOW') &#123;
                return (
                    <div class='list-view-center'>
                        &#123;slots.loading ? (
                            slots.loading()
                        ) : (
                            <div class='list-view-center' onClick=&#123;clickErrorText&#125;>
                                加载中...
                            </div>
                        )&#125;
                    </div>
                );
            &#125;
        &#125;;


        return () => &#123;
            const Content = contentList();
            const Placeholder = <div ref=&#123;placeholder&#125;  />;
            return (
                <div ref=&#123;root&#125; role="feed" >
                    &#123;props.direction === 'down' ? Content : Placeholder&#125;
                    &#123;renderLoading()&#125;
                    &#123;renderFinishedText()&#125;
                    &#123;renderErrorText()&#125;
                    &#123;props.direction === 'up' ? Content : Placeholder&#125;
                </div>
            );
        &#125;
    &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>list_view.css</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.list-view-center</span>&#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">flex-direction</span>: row;
    <span class="hljs-attribute">align-items</span>: center;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#777</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">15px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>skeleton.css 和CalmView 的一样，具体介绍可点击<a href="https://juejin.cn/post/6945748911147450405" target="_blank">这里</a>查看</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.skeleton-view-default-view</span> <span class="hljs-selector-tag">span</span>,
<span class="hljs-selector-class">.skeleton-view-default-view</span> <span class="hljs-selector-tag">a</span>,
<span class="hljs-selector-class">.skeleton-view-default-view</span> <span class="hljs-selector-tag">img</span>
&#123;
    <span class="hljs-attribute">transition</span>: all .<span class="hljs-number">7s</span> ease;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
&#125;

<span class="hljs-selector-class">.skeleton-view-empty-view</span> &#123;
    <span class="hljs-attribute">pointer-events</span>: none;
&#125;
<span class="hljs-selector-class">.skeleton-view-empty-view</span> <span class="hljs-selector-tag">span</span>,
<span class="hljs-selector-class">.skeleton-view-empty-view</span> <span class="hljs-selector-tag">a</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>) <span class="hljs-meta">!important</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">2px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(
            -<span class="hljs-number">45deg</span>,
            <span class="hljs-number">#F5F5F5</span> <span class="hljs-number">0%</span>,
            <span class="hljs-number">#DCDCDC</span> <span class="hljs-number">25%</span>,
            <span class="hljs-number">#F5F5F5</span> <span class="hljs-number">50%</span>,
            <span class="hljs-number">#DCDCDC</span> <span class="hljs-number">75%</span>,
            <span class="hljs-number">#F5F5F5</span> <span class="hljs-number">100%</span>
    );
    <span class="hljs-attribute">animation</span>: gradientBG <span class="hljs-number">4s</span> ease infinite;
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">400%</span> <span class="hljs-number">400%</span>;
    <span class="hljs-attribute">background-color</span>:<span class="hljs-number">#DCDCDC</span>;
    <span class="hljs-attribute">transition</span>: all <span class="hljs-number">1s</span> ease;
&#125;
<span class="hljs-comment">/* [src=""],img:not([src])*/</span>
<span class="hljs-selector-class">.skeleton-view-empty-view</span> <span class="hljs-selector-tag">img</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">../../assets/img/no_url.png</span>);// 一张空白的图片，可自行替换
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">2px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(
            -<span class="hljs-number">45deg</span>,
            <span class="hljs-number">#F5F5F5</span> <span class="hljs-number">0%</span>,
            <span class="hljs-number">#DCDCDC</span> <span class="hljs-number">25%</span>,
            <span class="hljs-number">#F5F5F5</span> <span class="hljs-number">50%</span>,
            <span class="hljs-number">#DCDCDC</span> <span class="hljs-number">75%</span>,
            <span class="hljs-number">#F5F5F5</span> <span class="hljs-number">100%</span>
    );
    <span class="hljs-attribute">animation</span>: gradientBG <span class="hljs-number">4s</span> ease infinite;
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">400%</span> <span class="hljs-number">400%</span>;
    <span class="hljs-attribute">background-color</span>:<span class="hljs-number">#DCDCDC</span>;
    <span class="hljs-attribute">transition</span>: all <span class="hljs-number">1s</span> ease;
&#125;
<span class="hljs-keyword">@keyframes</span> gradientBG &#123;
    <span class="hljs-number">0%</span> &#123;
        <span class="hljs-attribute">background-position</span>: <span class="hljs-number">100%</span> <span class="hljs-number">100%</span>;
    &#125;
    <span class="hljs-number">50%</span> &#123;
        <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0%</span> <span class="hljs-number">0%</span>;
    &#125;
    <span class="hljs-number">100%</span> &#123;
        <span class="hljs-attribute">background-position</span>: <span class="hljs-number">100%</span> <span class="hljs-number">100%</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">相关工具类(全都是复制的vant里的工具类，如有侵权，请联系我删除)</h4>
<ul>
<li>isHidden</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; unref, Ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isHidden</span>(<span class="hljs-params">
  elementRef: HTMLElement | Ref<HTMLElement | <span class="hljs-literal">undefined</span>>
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> el = unref(elementRef);
  <span class="hljs-keyword">if</span> (!el) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;

  <span class="hljs-keyword">const</span> style = <span class="hljs-built_in">window</span>.getComputedStyle(el);
  <span class="hljs-keyword">const</span> hidden = style.display === <span class="hljs-string">'none'</span>;

  <span class="hljs-comment">// offsetParent returns null in the following situations:</span>
  <span class="hljs-comment">// 1. The element or its parent element has the display property set to none.</span>
  <span class="hljs-comment">// 2. The element has the position property set to fixed</span>
  <span class="hljs-keyword">const</span> parentHidden = el.offsetParent === <span class="hljs-literal">null</span> && style.position !== <span class="hljs-string">'fixed'</span>;
  <span class="hljs-keyword">return</span> hidden || parentHidden;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>useRect</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Ref, unref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isWindow</span>(<span class="hljs-params">val: unknown</span>): <span class="hljs-title">val</span> <span class="hljs-title">is</span> <span class="hljs-title">Window</span> </span>&#123;
  <span class="hljs-keyword">return</span> val === <span class="hljs-built_in">window</span>;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useRect = <span class="hljs-function">(<span class="hljs-params">
  elementRef: (Element | Window) | Ref<Element | Window | <span class="hljs-literal">undefined</span>>
</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> element = unref(elementRef);

  <span class="hljs-keyword">if</span> (isWindow(element)) &#123;
    <span class="hljs-keyword">const</span> width = element.innerWidth;
    <span class="hljs-keyword">const</span> height = element.innerHeight;

    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">top</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">left</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">right</span>: width,
      <span class="hljs-attr">bottom</span>: height,
      width,
      height,
    &#125;;
  &#125;
  <span class="hljs-keyword">if</span> (element && element.getBoundingClientRect) &#123;
    <span class="hljs-keyword">return</span> element.getBoundingClientRect();
  &#125;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">top</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">left</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">right</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">bottom</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">width</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">0</span>,
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>useEventListener</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Ref, unref, onUnmounted, onDeactivated &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> &#123; onMountedOrActivated &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../onMountedOrActivated'</span>;

<span class="hljs-keyword">const</span>  inBrowser = <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">'undefined'</span>;

<span class="hljs-keyword">let</span> supportsPassive = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">if</span> (inBrowser) &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> opts = &#123;&#125;;
    <span class="hljs-built_in">Object</span>.defineProperty(opts, <span class="hljs-string">'passive'</span>, &#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        supportsPassive = <span class="hljs-literal">true</span>;
      &#125;,
    &#125;);
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'test-passive'</span>, <span class="hljs-literal">null</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>, opts);
    <span class="hljs-comment">// eslint-disable-next-line no-empty</span>
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;&#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> UseEventListenerOptions = &#123;
  target?: EventTarget | Ref<EventTarget | <span class="hljs-literal">undefined</span>>;
  capture?: <span class="hljs-built_in">boolean</span>;
  passive?: <span class="hljs-built_in">boolean</span>;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useEventListener</span>(<span class="hljs-params">
  <span class="hljs-keyword">type</span>: <span class="hljs-built_in">string</span>,
  listener: EventListener,
  options: UseEventListenerOptions = &#123;&#125;
</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!inBrowser) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;

  <span class="hljs-keyword">const</span> &#123; target = <span class="hljs-built_in">window</span>, passive = <span class="hljs-literal">false</span>, capture = <span class="hljs-literal">false</span> &#125; = options;

  <span class="hljs-keyword">let</span> attached: <span class="hljs-built_in">boolean</span>;

  <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> element = unref(target);

    <span class="hljs-keyword">if</span> (element && !attached) &#123;
      element.addEventListener(
        <span class="hljs-keyword">type</span>,
        listener,
        supportsPassive ? &#123; capture, passive &#125; : capture
      );
      attached = <span class="hljs-literal">true</span>;
    &#125;
  &#125;;

  <span class="hljs-keyword">const</span> remove = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> element = unref(target);

    <span class="hljs-keyword">if</span> (element && attached) &#123;
      element.removeEventListener(<span class="hljs-keyword">type</span>, listener, capture);
      attached = <span class="hljs-literal">false</span>;
    &#125;
  &#125;;

  onUnmounted(remove);
  onDeactivated(remove);
  onMountedOrActivated(add);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>useScrollParent</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; ref, Ref, onMounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;

<span class="hljs-keyword">type</span> ScrollElement = HTMLElement | Window;

<span class="hljs-keyword">const</span> overflowScrollReg = <span class="hljs-regexp">/scroll|auto/i</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isElement</span>(<span class="hljs-params">node: Element</span>) </span>&#123;
  <span class="hljs-keyword">const</span> ELEMENT_NODE_TYPE = <span class="hljs-number">1</span>;
  <span class="hljs-keyword">return</span> (
    node.tagName !== <span class="hljs-string">'HTML'</span> &&
    node.tagName !== <span class="hljs-string">'BODY'</span> &&
    node.nodeType === ELEMENT_NODE_TYPE
  );
&#125;

<span class="hljs-comment">// https://github.com/youzan/vant/issues/3823</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getScrollParent</span>(<span class="hljs-params">el: Element, root: ScrollElement = <span class="hljs-built_in">window</span></span>) </span>&#123;
  <span class="hljs-keyword">let</span> node = el;

  <span class="hljs-keyword">while</span> (node && node !== root && isElement(node)) &#123;
    <span class="hljs-keyword">const</span> &#123; overflowY &#125; = <span class="hljs-built_in">window</span>.getComputedStyle(node);
    <span class="hljs-keyword">if</span> (overflowScrollReg.test(overflowY)) &#123;
      <span class="hljs-keyword">return</span> node;
    &#125;
    node = node.parentNode <span class="hljs-keyword">as</span> Element;
  &#125;

  <span class="hljs-keyword">return</span> root;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useScrollParent</span>(<span class="hljs-params">el: Ref<Element | <span class="hljs-literal">undefined</span>></span>) </span>&#123;
  <span class="hljs-keyword">const</span> scrollParent = ref<Element | Window>();

  onMounted(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (el.value) &#123;
      scrollParent.value = getScrollParent(el.value);
    &#125;
  &#125;);

  <span class="hljs-keyword">return</span> scrollParent;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>onMountedOrActivated</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; nextTick, onMounted, onActivated &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onMountedOrActivated</span>(<span class="hljs-params">hook: () => <span class="hljs-built_in">any</span></span>) </span>&#123;
  <span class="hljs-keyword">let</span> mounted: <span class="hljs-built_in">boolean</span>;

  onMounted(<span class="hljs-function">() =></span> &#123;
    hook();
    nextTick(<span class="hljs-function">() =></span> &#123;
      mounted = <span class="hljs-literal">true</span>;
    &#125;);
  &#125;);

  onActivated(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (mounted) &#123;
      hook();
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            