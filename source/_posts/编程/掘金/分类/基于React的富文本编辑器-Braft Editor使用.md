
---
title: '基于React的富文本编辑器-Braft Editor使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76f9624fde24de1ae310a945db670cf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 19:31:25 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76f9624fde24de1ae310a945db670cf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>antd</code> 是基于 Ant Design 设计规范实现的 高质量 React 组件库，我们倾向于只提供符合该规范且带有视觉展现的 UI 组件，也尽量不重复造轮子。</p>
<p>如果要在React项目中使用富文本编辑器，官方推荐使用react-quill 与 braft-editor。
<a href="https://ant.design/docs/react/recommendation-cn" target="_blank" rel="nofollow noopener noreferrer">详细点击这里</a></p>
<p>这篇文章主要介绍Braft Editor与Antd的结合使用。</p>
<h2 data-id="heading-0">在Ant Design表单中使用</h2>
<h3 data-id="heading-1">功能要点</h3>
<ul>
<li>使用<code>BraftEditor.createEditorState</code>创建editorState</li>
<li>使用<code>editorState.toHTML()</code>实时获取html</li>
<li>使用<code>editorState.isEmpty()</code>进行空值校验</li>
</ul>
<h3 data-id="heading-2">注意事项</h3>
<ul>
<li>编辑器组件的数据格式为ediorState，为此在调用setFieldsValue时和在提交之前，需要进行相应的转换（toHTML()）</li>
<li>进行空值校验的话，需要自定义validator，并通过value.isEmpty()来校验，value就是一个editorState</li>
<li>编辑器组件的验证时机需要改成onBlur，以避免不期望的验证提示和不必要的性能开销</li>
<li>编辑器的value属性必须是一个editorState对象</li>
<li>实际使用时请避免在onChange中直接toHTML，配合节流函数或者在合适的时机使用更恰当</li>
</ul>
<h3 data-id="heading-3">编辑器演示</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76f9624fde24de1ae310a945db670cf~tplv-k3u1fbpfcp-watermark.image" alt="WX20210517-111254@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">示例源码</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> BaseCmp <span class="hljs-keyword">from</span> <span class="hljs-string">'@components/BaseCmp.js'</span>
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>
<span class="hljs-keyword">import</span> &#123;
    RLInput, RLButton, RLForm, RLFormItem
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@components/index.js'</span>
<span class="hljs-keyword">import</span> &#123; DatePicker &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>
<span class="hljs-keyword">import</span> &#123; createRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> BraftEditor <span class="hljs-keyword">from</span> <span class="hljs-string">'braft-editor'</span>
<span class="hljs-keyword">import</span> actionInfoManage <span class="hljs-keyword">from</span> <span class="hljs-string">'@actions/infoManage/actionInfoManage.js'</span>
<span class="hljs-keyword">import</span> &#123; dealTime, dealDateTime &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/libs/utils.js'</span>
<span class="hljs-keyword">import</span> moment <span class="hljs-keyword">from</span> <span class="hljs-string">'moment'</span>
<span class="hljs-keyword">import</span> locale <span class="hljs-keyword">from</span> <span class="hljs-string">'antd/es/date-picker/locale/zh_CN'</span>


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CmpInfoEdit</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">BaseCmp</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(props)
        <span class="hljs-keyword">if</span> (props.infoId) &#123;
            <span class="hljs-built_in">this</span>.infoId = props.infoId
        &#125;
        <span class="hljs-built_in">this</span>.state = &#123;
            <span class="hljs-attr">infoListInfo</span>: &#123;
                <span class="hljs-attr">title</span>: <span class="hljs-string">''</span>,
                <span class="hljs-attr">start_time</span>: <span class="hljs-string">''</span>,
                <span class="hljs-attr">content</span>: BraftEditor.createEditorState(<span class="hljs-literal">null</span>)
            &#125;
        &#125;
        <span class="hljs-built_in">this</span>.form = createRef()
    &#125;
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.infoId) &#123;   <span class="hljs-comment">// 编辑</span>
            <span class="hljs-built_in">this</span>.getInfoDetail(<span class="hljs-built_in">this</span>.infoId)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.setState(&#123;
                <span class="hljs-attr">infoListInfo</span>: &#123;
                    ...this.state.infoListInfo
                &#125;
            &#125;)
        &#125;
    &#125;

    <span class="hljs-comment">// 资讯详情</span>
    getInfoDetail = <span class="hljs-function">(<span class="hljs-params">id</span>) =></span> &#123;
        actionInfoManage.getInfoDetail(&#123;id&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (res.code === <span class="hljs-number">200</span>) &#123;
                <span class="hljs-keyword">const</span> data = res.data
                <span class="hljs-keyword">let</span> userList = data.invite_uids
                <span class="hljs-built_in">this</span>.setState(&#123;
                    userList,
                    <span class="hljs-attr">infoListInfo</span>: &#123;
                        ...data,
                        <span class="hljs-attr">start_time</span>: moment(dealTime(data.start_time, <span class="hljs-string">'YYYY-MM-DD HH:mm'</span>)),
                        <span class="hljs-attr">content</span>: BraftEditor.createEditorState(data.content),
                    &#125;
                &#125;, <span class="hljs-function">() =></span> &#123;
                    <span class="hljs-comment">// 给表单重置值</span>
                    <span class="hljs-built_in">this</span>.form && <span class="hljs-built_in">this</span>.form.setFieldsValue(<span class="hljs-built_in">this</span>.state.infoListInfo)
                &#125;)
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-built_in">this</span>.showToast(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'error'</span>, <span class="hljs-attr">content</span>: res.msg &#125;)
            &#125;
        &#125;)
    &#125;

    editFailed = <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.showToast(&#123; <span class="hljs-attr">content</span>: <span class="hljs-string">'您有必填项未填写'</span>, <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span> &#125;)
    &#125;

    editConfirm = <span class="hljs-function">(<span class="hljs-params">values</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onFinish'</span>, values)
        <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">addLoading</span>: <span class="hljs-literal">true</span>
        &#125;)
        <span class="hljs-keyword">let</span> &#123; start_time &#125; = values
        <span class="hljs-keyword">const</span> &#123; title, content &#125; = <span class="hljs-built_in">this</span>.state.infoListInfo
        <span class="hljs-keyword">const</span> params = &#123;
            title,
            <span class="hljs-attr">start_time</span>: dealDateTime(start_time.format(<span class="hljs-string">'YYYY-MM-DD HH:mm'</span>)),
            <span class="hljs-attr">content</span>: content.toHTML()
        &#125;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.infoId) &#123;   <span class="hljs-comment">// 编辑</span>
            actionInfoManage.infoEdit(&#123; ...params, <span class="hljs-attr">id</span>: <span class="hljs-built_in">this</span>.infoId &#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                <span class="hljs-keyword">if</span> (res.code === <span class="hljs-number">200</span>) &#123;
                    <span class="hljs-built_in">this</span>.showToast(&#123; <span class="hljs-attr">content</span>: <span class="hljs-string">'编辑成功'</span>, <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span> &#125;)
                    <span class="hljs-built_in">this</span>.props.changePage(<span class="hljs-string">'list'</span>)
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-built_in">this</span>.showToast(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'error'</span>, <span class="hljs-attr">content</span>: res.msg &#125;)
                &#125;
            &#125;).finally(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-built_in">this</span>.setState(&#123;
                    <span class="hljs-attr">addLoading</span>: <span class="hljs-literal">false</span>
                &#125;)
            &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;   <span class="hljs-comment">// 创建</span>
            actionInfoManage.infoAdd(params).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                <span class="hljs-keyword">if</span> (res.code === <span class="hljs-number">200</span>) &#123;
                    <span class="hljs-built_in">this</span>.showToast(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>, <span class="hljs-attr">content</span>: <span class="hljs-string">'创建成功'</span> &#125;)
                    <span class="hljs-built_in">this</span>.props.changePage(<span class="hljs-string">'list'</span>)
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-built_in">this</span>.showToast(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'error'</span>, <span class="hljs-attr">content</span>: res.msg &#125;)
                &#125;
            &#125;).finally(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-built_in">this</span>.setState(&#123;
                    <span class="hljs-attr">addLoading</span>: <span class="hljs-literal">false</span>
                &#125;)
            &#125;)
        &#125;
    &#125;

    disabledDate = <span class="hljs-function">(<span class="hljs-params">current</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> current && current < moment().startOf(<span class="hljs-string">'day'</span>)
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'page-info-edit'</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">RLForm</span>
                    <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;form</span> =></span> this.form = form&#125;
                    labelCol=&#123;&#123; style: &#123; width: 150, marginRight: 20, textAlign: 'right' &#125; &#125;&#125;
                    labelAlign='left'
                    wrapperCol=&#123;&#123; style: &#123; span: 24, marginRight: 30 &#125; &#125;&#125;
                    onFinish=&#123;this.editConfirm&#125;
                    onFinishFailed=&#123;this.editFailed&#125;
                    initialValues=&#123;this.state.infoListInfo&#125;
                    validateTrigger='onBlur'
                >
                    <span class="hljs-tag"><<span class="hljs-name">RLFormItem</span>
                        <span class="hljs-attr">name</span>=<span class="hljs-string">'title'</span>
                        <span class="hljs-attr">label</span>=<span class="hljs-string">'资讯主题'</span>
                        <span class="hljs-attr">colon</span>=<span class="hljs-string">&#123;false&#125;</span>
                        <span class="hljs-attr">rules</span>=<span class="hljs-string">&#123;[</span>
                            &#123;
                                <span class="hljs-attr">required:</span> <span class="hljs-attr">true</span>,
                                <span class="hljs-attr">message:</span> '请输入资讯主题'
                            &#125;, &#123;
                                <span class="hljs-attr">max:</span> <span class="hljs-attr">50</span>,
                                <span class="hljs-attr">message:</span> '资讯主题最多<span class="hljs-attr">50</span>个字符'
                            &#125;
                        ]&#125;
                    ></span>
                        <span class="hljs-tag"><<span class="hljs-name">RLInput</span>
                            <span class="hljs-attr">placeholder</span>=<span class="hljs-string">'请输入资讯主题'</span>
                            <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> <span class="hljs-attr">360</span> &#125;&#125;
                            <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;this.state.infoListInfo.title&#125;</span>
                            <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;e</span> =></span> &#123;
                                this.setState(&#123;
                                    infoListInfo: &#123;
                                        ...this.state.infoListInfo,
                                        title: e.target.value
                                    &#125;
                                &#125;)
                            &#125;&#125;
                        />
                    <span class="hljs-tag"></<span class="hljs-name">RLFormItem</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">RLFormItem</span>
                        <span class="hljs-attr">name</span>=<span class="hljs-string">'start_time'</span>
                        <span class="hljs-attr">label</span>=<span class="hljs-string">'发布时间'</span>
                        <span class="hljs-attr">colon</span>=<span class="hljs-string">&#123;false&#125;</span>
                        <span class="hljs-attr">rules</span>=<span class="hljs-string">&#123;[</span>
                            &#123;
                                <span class="hljs-attr">required:</span> <span class="hljs-attr">true</span>,
                                <span class="hljs-attr">message:</span> '请选择发布时间'
                            &#125;
                        ]&#125;
                    ></span>
                        <span class="hljs-tag"><<span class="hljs-name">DatePicker</span>
                            <span class="hljs-attr">allowClear</span>
                            <span class="hljs-attr">locale</span>=<span class="hljs-string">&#123;locale&#125;</span>
                            <span class="hljs-attr">showTime</span>
                            <span class="hljs-attr">disabledDate</span>=<span class="hljs-string">&#123;this.disabledDate&#125;</span>
                            <span class="hljs-attr">format</span>=<span class="hljs-string">&#123;</span>'<span class="hljs-attr">YYYY-MM-DD</span> <span class="hljs-attr">HH:mm</span>'&#125;
                            <span class="hljs-attr">placeholder</span>=<span class="hljs-string">'请选择日期时间'</span>
                        /></span>
                    <span class="hljs-tag"></<span class="hljs-name">RLFormItem</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">RLFormItem</span>
                        <span class="hljs-attr">name</span>=<span class="hljs-string">'content'</span>
                        <span class="hljs-attr">label</span>=<span class="hljs-string">'正文内容'</span>
                        <span class="hljs-attr">colon</span>=<span class="hljs-string">&#123;false&#125;</span>
                        <span class="hljs-attr">rules</span>=<span class="hljs-string">&#123;[</span>
                            &#123;
                                <span class="hljs-attr">required:</span> <span class="hljs-attr">true</span>,
                                <span class="hljs-attr">validator:</span> (<span class="hljs-attr">rule</span>, <span class="hljs-attr">value</span>) =></span> &#123;
                                    if (value.isEmpty()) &#123;
                                        return Promise.reject('请输入正文内容')
                                    &#125; else &#123;
                                        return Promise.resolve()
                                    &#125;
                                &#125;
                            &#125;
                        ]&#125;
                    >
                        <span class="hljs-tag"><<span class="hljs-name">BraftEditor</span>
                            <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;this.state.infoListInfo.content&#125;</span>
                            <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;editorState</span> =></span> &#123;
                                this.setState(&#123;
                                    infoListInfo: &#123;
                                        ...this.state.infoListInfo,
                                        content: editorState
                                    &#125;
                                &#125;)
                            &#125;&#125;
                            media=&#123;&#123;
                                accepts: &#123;
                                    image: 'image/jpeg,image/png',
                                    video: 'video/mp4',
                                    audio: 'audio/mpeg,audio/mp3',
                                &#125;,
                                uploadFn: (upload) => &#123;&#125;,

                                // onChange(...rest) &#123;
                                //     console.log('onChange---rest', rest)
                                // &#125;
                            &#125;&#125;
                            style=&#123;&#123; border: '1px solid #d1d1d1', borderRadius: 3, background: '#fff' &#125;&#125;
                        />
                    <span class="hljs-tag"></<span class="hljs-name">RLFormItem</span>></span>

                    <span class="hljs-tag"><<span class="hljs-name">RLFormItem</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">display:</span> '<span class="hljs-attr">flex</span>', <span class="hljs-attr">justifyContent:</span> '<span class="hljs-attr">center</span>' &#125;&#125;></span>
                            <span class="hljs-tag"><<span class="hljs-name">RLButton</span>
                                <span class="hljs-attr">type</span>=<span class="hljs-string">"default"</span>
                                <span class="hljs-attr">label</span>=<span class="hljs-string">'取消'</span>
                                <span class="hljs-attr">width</span>=<span class="hljs-string">&#123;80&#125;</span>
                                <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">display:</span> '<span class="hljs-attr">inline-block</span>' &#125;&#125;
                                <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
                                    this.props.changePage('list')
                                &#125;&#125;
                            />
                            <span class="hljs-tag"><<span class="hljs-name">RLButton</span>
                                <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>
                                <span class="hljs-attr">htmlType</span>=<span class="hljs-string">"submit"</span>
                                <span class="hljs-attr">label</span>=<span class="hljs-string">&#123;this.infoId</span> ? '保存' <span class="hljs-attr">:</span> '创建'&#125;
                                <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">marginLeft:</span> <span class="hljs-attr">40</span>, <span class="hljs-attr">display:</span> '<span class="hljs-attr">inline-block</span>' &#125;&#125;
                                <span class="hljs-attr">loading</span>=<span class="hljs-string">&#123;this.state.addLoading&#125;</span>
                                <span class="hljs-attr">width</span>=<span class="hljs-string">&#123;80&#125;</span>
                            /></span>

                        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

                    <span class="hljs-tag"></<span class="hljs-name">RLFormItem</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">RLForm</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;

&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(<span class="hljs-function">(<span class="hljs-params">store, props</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        ...props
    &#125;
&#125;)(CmpInfoEdit)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">空值校验</h3>
<p>使用<code>isEmpty()</code>校验，rules中的代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">rules=&#123;[
    &#123;
        <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">validator</span>: <span class="hljs-function">(<span class="hljs-params">rule, value</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (value.isEmpty()) &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">'请输入正文内容'</span>)
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve()
            &#125;
        &#125;
    &#125;
]&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            