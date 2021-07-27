
---
title: '关于使用Sortable来实现表格的拖拽遇到的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4393f98f988a4a14bea97a9e7d77ec74~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 01:56:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4393f98f988a4a14bea97a9e7d77ec74~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";@keyframes spin&#123;0%&#123;transform:rotate(0)&#125;to&#123;transform:rotate(1turn)&#125;&#125;.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#36ace1;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;color:#36ace1&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"";display:block;position:absolute;left:0;top:0;bottom:0;margin:auto;background-image:url(data:image/png;base64,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);animation:spin 2s linear 1s infinite&#125;.markdown-body h1&#123;position:relative;font-size:30px;padding:12px 38px;margin:30px 0&#125;.markdown-body h1:before&#123;width:30px;height:30px;background-size:30px 30px&#125;.markdown-body h2&#123;position:relative;font-size:24px;padding:12px 36px;margin:28px 0&#125;.markdown-body h2:before&#123;width:28px;height:28px;background-size:28px 28px&#125;.markdown-body h3&#123;position:relative;font-size:18px;padding:4px 32px;margin:26px 0&#125;.markdown-body h3:before&#123;width:24px;height:24px;background-size:24px 24px&#125;.markdown-body h4&#123;position:relative;padding:4px 28px;font-size:16px;margin:22px 0&#125;.markdown-body h4:before&#123;width:20px;height:20px;background-size:20px 20px&#125;.markdown-body h5&#123;position:relative;padding:4px 26px;font-size:15px;margin:20px 0&#125;.markdown-body h5:before&#123;width:18px;height:18px;background-size:18px 18px&#125;.markdown-body h6&#123;position:relative;padding:4px 22px;font-size:14px;margin:16px 0&#125;.markdown-body h6:before&#123;width:16px;height:16px;background-size:16px 16px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#36ace1,#dff0fe,#36ace1);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:50px;height:24px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAEgElEQVRIS72Va0xbZRjH/z2FcimbchEQFDYRCIRAAWFQ2MaCXBwmUxYDLGGEcRFkH9wmk04zG0Bo2dwNIisERANqhjqdEmhd4nRbuwpsXDYWLLoRgeG4Chu9QHvMOQ0dpTAKH3y/tDnv8/5/z/Oc//scBv6nxdgoJ14gVYPEuITHdTdHY12gRIH0T0KljlqwthqUFHGtzAEsxqwLtPvkdc+FeeI3BgMeAMEhdOqR1mM7xswBrgmKE8pfIUhtm7fbZsft/i7wc98MtrUFxmbU6ByYgFwxjtFp5Q+WpF1mCy9wajXoqqD4E91saOf603e+5B7t99xTkyZJEiKJAl2DE9Xio1HvrBS8IuhVwVUP503swdJ9QWAw1izaoDs6pQT/655BMS9yy3KYiUoM/7adu7NmtnQfx5zWm8Q8Ui3gyGcddyU8rv/STRNQouDGP5/mhTubX4dpPv3DMzh1qS9LwuPWr+i63WVyn5QYj/4d/i4bqmbpoQ+auvBlQYghX6PE4wTSOzV5EUYlb5Q4MDqLk9/3cMRF27spDSNQamUnWZ4ebNB+OKNCyYVeFCZ5wZ5tiePN/UiP2YoQL0cUX+iFt4sNUiLdcaVvHJLecQiWnKVE8s5LvxAXRWeYgHLre0hecgAN0sxr0XBZgbJUP6OiLnaM4ivZCBrzOWBZEIY9rY5E8pl2nM0KMzzLq5aPiXmRzgbQm2VyR8KGGK/ICAFB6IusbvsDwhRf+n/jtSHc/nsGgjR9V6/1TyLa1wGU+FtnO1CbHQTHTSzIFJOYJ1jwcGLTccMTcyhp7oW4KFJ/SV4/IScrc55kQj07WNuOn94Lpw8kCm/Qv3W5HLjbWxsyfuNUO1TzWjAJBloKt2FBS+Jz6ShiA12NupBdLWugQcmn28lPMkONNql3U5cTSD9Lq+qEUqPFt++G0aKL687wDAqb+pAU7IKCuK2493AOPQ9UCNpib6T1tkg+RZ9KKJcNn8sJc1vac8o16jklLWLuOiDqwvHUIKPw7vtTON+iCDKkl/Cx9FeSYET5um1mHt6jN0Dz9ftwYjORudNjTdaBmi7kxvvA1d6Gjs0X/Q5Sp3tMEMSHre9HnDEZAPFCWUNVdliGJVPvqEP1Hbh4yPj9LadSY6fu6gPsCX+B3mq7NYLv2od8fj4aoViMNQGFijos/XVMTXGavgUisQIle71hwVx9KFEutLVjw8GORTuxoEbeJS7iPrmQyy/sIj2hQpqYHO7ZGs95nnZS4y8K8Pfqrb58UZ+IlKqbqNgfQm8da+pC9xjLqo8foFkau2qaCeXSyvzXfA9SDrp1bxJ/DU/jSJKXEWdBR2J/9U0UpwXTFZ/+8S76h/71FvO4A8sTeuqQThDKalOiPLN3BbhiYlaNsm964elkCztrC4xMqeDqYIus2JdB3cbS5l4MTag44qJt9GxbF4gKThRKY59lW13+KCUQ1pZMEwHKviKx4pFSqXzxCn/X9Gr2NO+zw+cTiTbxmUyCqH3GlsWg2kRNhOnHmhlrFkIvHTZt1borWvMCmRnwH4usn58STiycAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body del&#123;color:#36ace1&#125;.markdown-body code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#282c34;color:#4ec9b0;padding:.24em .46em;margin:0 4px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;font-size:12px;border-radius:10px;padding:15px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#4ec9b0;background:#282c34&#125;.markdown-body a&#123;text-decoration:none;color:#409eff;border-bottom:1px solid #409eff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#007bff;border-bottom:1px solid #007bff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;position:relative;padding:8px 26px;background-color:rgba(54,172,225,.75);margin:16px 0;border-left:4px solid #409eff;border-radius:5px&#125;.markdown-body blockquote:before&#123;content:"❝";top:10px;left:8px;color:#409eff;font-size:20px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:20px;position:absolute;right:8px;bottom:0;color:#409eff;opacity:.7&#125;.markdown-body blockquote>p&#123;color:#fff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">引入</h3>
<blockquote>
<p>npm install sortablejs --save</p>
</blockquote>
<p>按需引入</p>
<blockquote>
<p>import Sortable from 'sortablejs';</p>
</blockquote>
<h3 data-id="heading-1">方法一：</h3>
<h4 data-id="heading-2">1.首先是拖拽完成之后需要重新调用列表的接口</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4393f98f988a4a14bea97a9e7d77ec74~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">2.el-table里面绑定一个key，在刷新数据的时候取反</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4660d364c7414f678dd8a3e105be36ff~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">方法二：</h3>
<p>异步再次执行一次表格数据的赋值，推荐使用这种，看似呆板，但是易懂！！！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ae6e4c2c6014443a140c6a145d8a6c1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b1a4e892fda4aa587779cce8c2df8a8~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">注意：</h3>
<p>这里排序会调用一个接口，我们不要忽略了接口调用失败的数据处理，不然数据的顺序会改变与后台的数据不一致</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbc0345840544a0086aebcbde348f804~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"department-manu"</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">el-table</span>
            <span class="hljs-attr">ref</span>=<span class="hljs-string">"itsmDataTable"</span>
            <span class="hljs-attr">:data</span>=<span class="hljs-string">"tableData"</span>
            <span class="hljs-attr">stripe</span>
            <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%; font-size: 16px;"</span>
            <span class="hljs-attr">:row-style</span>=<span class="hljs-string">"&#123;'font-size':'14px','height':'46px'&#125;"</span>
        ></span>
            <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"selection"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"index"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"70"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"序号"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"DEPARTNAME"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"部门名称"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"DEPARTDESC"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"部门描述"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"TRUENAME"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"创建人"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">align</span>=<span class="hljs-string">"center"</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"CRTIME"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"创建时间"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"165"</span>></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> Sortable <span class="hljs-keyword">from</span> <span class="hljs-string">'sortablejs'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'DepartmentMenu'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">tableData</span>: [], <span class="hljs-comment">// 部门列表</span>
        &#125;;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.getTableData();
    &#125;,
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.rowDrop();
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-comment">/**
         * [getTableData description]获取部门列表
         *
         * <span class="hljs-doctag">@param   <span class="hljs-type">&#123;[type]&#125;</span>  </span>str  [str description]
         *
         * <span class="hljs-doctag">@return  <span class="hljs-type">&#123;[type]&#125;</span>       </span>[return description]
         */</span>
        <span class="hljs-function"><span class="hljs-title">getTableData</span>(<span class="hljs-params">str = <span class="hljs-string">''</span></span>)</span> &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-built_in">this</span>.$route.query) !== <span class="hljs-string">'&#123;&#125;'</span>) &#123;
                <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'***********'</span>, &#123;
                    <span class="hljs-attr">params</span>: &#123;***********&#125;,
                &#125;).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
                    <span class="hljs-keyword">const</span> msg = data.DATA || data;
                    <span class="hljs-comment">// 防止拖拽排序抖动</span>
                    <span class="hljs-keyword">const</span> copyData = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(msg));
                    <span class="hljs-built_in">this</span>.tableData = [];
                    <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
                        <span class="hljs-built_in">this</span>.tableData = copyData;
                    &#125;);
                    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.$route.query.parentid || <span class="hljs-built_in">this</span>.$route.query.parentid * <span class="hljs-number">1</span> === <span class="hljs-number">0</span>) &#123;
                        <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'refresh'</span>);
                    &#125;
                &#125;);
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-built_in">this</span>.tableData = [];
            &#125;
        &#125;,




        <span class="hljs-comment">/**
         * [拖动排序]]
         *
         * <span class="hljs-doctag">@return  <span class="hljs-type">&#123;[type]&#125;</span>  </span>[return description]
         */</span>
        <span class="hljs-function"><span class="hljs-title">rowDrop</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">const</span> tbody = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.el-table__body-wrapper tbody'</span>);
            <span class="hljs-built_in">this</span>.sortable = Sortable.create(tbody, &#123;
                <span class="hljs-attr">onEnd</span>: <span class="hljs-function"><span class="hljs-params">evt</span> =></span> &#123; <span class="hljs-comment">// 拖动结束时触发，我在这里调用接口，改变后台的排序</span>
                    <span class="hljs-keyword">if</span> (evt.oldIndex !== evt.newIndex) &#123;
                        <span class="hljs-keyword">const</span> params = &#123;*******&#125;;
                        <span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">'****'</span>, &#123; <span class="hljs-attr">params</span>: params &#125;).then(<span class="hljs-function">() =></span> &#123;
                            <span class="hljs-built_in">this</span>.getTableData();
                        &#125;).catch(<span class="hljs-function">() =></span> &#123;
                            <span class="hljs-keyword">const</span> copyData = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-built_in">this</span>.tableData));
                            <span class="hljs-built_in">this</span>.TABLE_DATA_GROUP = [];
                            <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
                                <span class="hljs-built_in">this</span>.tableData = copyData;
                            &#125;);
                        &#125;);
                    &#125;
                &#125;,
            &#125;);
        &#125;,
    &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>


<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            