
---
title: '【YcDynamicForm文档】前端动态表单（一套配置_多套UI） - 戴向天'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7598'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 00:24:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=7598'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好！我叫戴向天</p>
<p>QQ群：602504799</p>
<p>如若有不理解的，可加QQ群进行咨询了解</p>
<h1 data-id="heading-0">yc-dynamic-form</h1>
<h2 data-id="heading-1"><strong>Introduction</strong></h2>
<p>文档编辑者：戴向天 / 白玺东</p>
<p>更新时间：2021 年 8 月 8 日</p>
<p>动态表单企鹅群： <em><strong>877965995</strong></em></p>
<p>官方 Api 文档地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yangchan.work%2Fyc-dynamic-form" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yangchan.work/yc-dynamic-form" ref="nofollow noopener noreferrer">www.yangchan.work/yc-dynamic-…</a></p>
<h3 data-id="heading-2">优点</h3>
<ul>
<li>
<p><em><strong>只需要通过配置信息就可实现动态表单的生成,且满足大部分业务需求</strong></em></p>
</li>
<li>
<p><em><strong>实现一套配置兼容多套 UI，通过配置映射表（mapping）兼容自定义表单组件及大部份 UI 库的表单组件如：【Ant Design of Vue，element-ui】</strong></em></p>
</li>
<li>
<p><em><strong>表单配置项可动态修改</strong></em></p>
</li>
<li>
<p><em><strong>支持自定义组件及自定义事件扩展</strong></em></p>
</li>
<li>
<p><em><strong>支持数据填充时/数据获取时进行拦截处理</strong></em></p>
</li>
<li>
<p><em><strong>支持配置函数中 this 调用内置表单事件及全局事件（this 指向内置表单, 表单在 vue 下）</strong></em></p>
</li>
<li>
<p><em><strong>表单内置事件可链式调用</strong></em></p>
</li>
</ul>
<h3 data-id="heading-3">扩展</h3>
<ul>
<li><em><strong>开发者可以在配置信息上进行加上自己自定义的 key 名，从而去实现功能。为二次封装做下了良好的基础。</strong></em></li>
</ul>
<h2 data-id="heading-4">npm 安装</h2>
<pre><code class="copyable">npm install yc-dynamic-form
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">使用</h2>
<pre><code class="copyable">import YcDynamicForm from 'yc-dynamic-form'
Vue.use(YcDynamicForm)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">
<template>
  <YcDynamicForm :gutter="30" :config="config" :mapping="mapping" :format="format" />
</template>

<script>
import YcDynamicForm from "yc-dynamic-form";
import * as elementUI from "./mapping/element-mapping.js";
export default &#123;
  components: &#123;YcDynamicForm&#125;,
  data()&#123;
    return &#123;
      mapping: elementUI,
      format: elementUI.format,
      config: [
        &#123;
          children: [
            &#123;label: '姓名',type: 'input',prop: 'name'&#125;,
            &#123;label: '年龄',type: 'input',prop: 'age'&#125;,
          ]
        &#125;
      ]
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6"><strong><em>Attributes</em></strong></h2>





























































<table><thead><tr><th>参数</th><th>说明</th><th>类型</th><th>可选值</th><th>默认值</th></tr></thead><tbody><tr><td>config</td><td>表单的配置信息</td><td>array</td><td>-</td><td>[]</td></tr><tr><td>rules</td><td>效验规则，具体的参考相对应的 UI 框架</td><td>object</td><td>-</td><td>&#123;&#125;</td></tr><tr><td>gutter</td><td>默认的间距</td><td>number</td><td>-</td><td>null</td></tr><tr><td>layout</td><td>表单布局,根据自己选择的 UI 框架相对的布局参数</td><td>string</td><td>-</td><td>null</td></tr><tr><td>mapping</td><td>映射表</td><td>object</td><td>-</td><td>&#123;&#125;</td></tr><tr><td>format</td><td>数据格式化拦截器：set & get</td><td>object</td><td>-</td><td>-</td></tr><tr><td>parentName</td><td>父级的<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>o</mi><mi>p</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mi>s</mi><mi mathvariant="normal">.</mi><mi>n</mi><mi>a</mi><mi>m</mi><mi>e</mi><mtext>值，主要是用来获取对应的父级并做相对应的父级函数调用，之所以需要这个参数是因为防止在某些情况下，动态表单的</mtext></mrow><annotation encoding="application/x-tex">options.name值，主要是用来获取对应的父级并做相对应的父级函数调用，之所以需要这个参数是因为防止在某些情况下，动态表单的</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">o</span><span class="mord mathnormal">p</span><span class="mord mathnormal">t</span><span class="mord mathnormal">i</span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mord mathnormal">s</span><span class="mord">.</span><span class="mord mathnormal">n</span><span class="mord mathnormal">a</span><span class="mord mathnormal">m</span><span class="mord mathnormal">e</span><span class="mord cjk_fallback">值</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">主</span><span class="mord cjk_fallback">要</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">用</span><span class="mord cjk_fallback">来</span><span class="mord cjk_fallback">获</span><span class="mord cjk_fallback">取</span><span class="mord cjk_fallback">对</span><span class="mord cjk_fallback">应</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">父</span><span class="mord cjk_fallback">级</span><span class="mord cjk_fallback">并</span><span class="mord cjk_fallback">做</span><span class="mord cjk_fallback">相</span><span class="mord cjk_fallback">对</span><span class="mord cjk_fallback">应</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">父</span><span class="mord cjk_fallback">级</span><span class="mord cjk_fallback">函</span><span class="mord cjk_fallback">数</span><span class="mord cjk_fallback">调</span><span class="mord cjk_fallback">用</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">之</span><span class="mord cjk_fallback">所</span><span class="mord cjk_fallback">以</span><span class="mord cjk_fallback">需</span><span class="mord cjk_fallback">要</span><span class="mord cjk_fallback">这</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">参</span><span class="mord cjk_fallback">数</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">因</span><span class="mord cjk_fallback">为</span><span class="mord cjk_fallback">防</span><span class="mord cjk_fallback">止</span><span class="mord cjk_fallback">在</span><span class="mord cjk_fallback">某</span><span class="mord cjk_fallback">些</span><span class="mord cjk_fallback">情</span><span class="mord cjk_fallback">况</span><span class="mord cjk_fallback">下</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">动</span><span class="mord cjk_fallback">态</span><span class="mord cjk_fallback">表</span><span class="mord cjk_fallback">单</span><span class="mord cjk_fallback">的</span></span></span></span></span>parent 被嵌套多层，导致所获取的<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mo separator="true">,</mo><mtext>非正确的</mtext></mrow><annotation encoding="application/x-tex">parent,非正确的</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">p</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord cjk_fallback">非</span><span class="mord cjk_fallback">正</span><span class="mord cjk_fallback">确</span><span class="mord cjk_fallback">的</span></span></span></span></span>parent</td><td>string</td><td>-</td><td>-</td></tr></tbody></table>
<h2 data-id="heading-7"><strong><em>Mapping</em></strong></h2>





















































<table><thead><tr><th>参数</th><th>说明</th><th>是否未必选项</th><th>类型</th></tr></thead><tbody><tr><td>componentMapping</td><td>组件映射配置信息（键值对）。key 名就是自定义的组件名称，value：实际上的组件名称。 例如：&#123;'input': 'el-ipnut'&#125;</td><td>是</td><td>object</td></tr><tr><td>modelMapping</td><td>model 映射表（键值对）。key 名就是组件 model 的触发事件名称，value：componentMapping 的 key 名数组【】。由于不同 UI 框架的不同数据绑定方式，有些组件是通过 change 来触发 model，有的是通过 input 进行触发 model。&#123;'change'：[]&#125;</td><td>是</td><td>object</td></tr><tr><td>defaultValueMap</td><td>组件默认值（键值对）。key 名就是 componentMapping 的 key 名，value：默认值。例如：&#123;'input':''&#125;</td><td>否</td><td>object</td></tr><tr><td>placeholderMapping</td><td>组件 placeholder 处理. key 名就是 componentMapping 的 key 名,value: label 的前缀。 例如：&#123;'input':'请输入'&#125;</td><td>否</td><td>object</td></tr><tr><td>format</td><td>表单数据设置和获取的拦截处理。</td><td>否</td><td>object</td></tr><tr><td>format.set</td><td>表单数据设置拦截处理。注意的是：该方法的 this 指向是动态表单。共接受三个参数：key, value, type</td><td>否</td><td>function</td></tr><tr><td>format.get</td><td>表单数据获取的拦截处理。注意的是：该方法的 this 指向是动态表单</td><td>否</td><td>function</td></tr></tbody></table>
<h2 data-id="heading-8"><strong><em>Methods</em></strong></h2>







































































































































































<table><thead><tr><th>方法名</th><th>说明</th><th>参数</th><th>返回</th></tr></thead><tbody><tr><td>getForm</td><td>获取表单</td><td>-</td><td>返回当前的表单元素</td></tr><tr><td>getParent</td><td>获取父级节点，注意的是：需要依赖的就是需要在 props 里面告知 parentName 的值，也就是页面或者组件的 name 参数$options.name</td><td>-</td><td>返回父级节点，或者 null</td></tr><tr><td>runCreateHandler</td><td>运行每一项 events 中事件名称为 create 的事件信息，只触发一次</td><td>-</td><td>无</td></tr><tr><td>getCreateHandlerMap</td><td>获取每一项 events 中事件名称为 create 的事件信息</td><td>-</td><td>function[]</td></tr><tr><td>getConfigList</td><td>获取所有的配置信息</td><td>-</td><td>返回一个列表形式的配置信息: IConfigSign[]</td></tr><tr><td>getConfig</td><td>获取指定的配置信息</td><td>arr: IConfig, prop: string</td><td>IConfigSign</td></tr><tr><td>createNewConfig</td><td>信息配置信息,主要是防止配置信息的内存地址与新的配置信息一直，所影响到初始化的配置信息</td><td>IConfig</td><td>IConfig</td></tr><tr><td>trigger</td><td>主动触发指定的 prop 的配置信息中的指定事件</td><td>prop: string, eventName: string</td><td>this</td></tr><tr><td>setLocalParams</td><td>设置当前表单的作用域数据信息</td><td>key: string, value: any</td><td>this</td></tr><tr><td>setLocalParamsMap</td><td>批量设置当前表单的作用域数据信息</td><td>&#123; key: string,value: any &#125;[]</td><td>this</td></tr><tr><td>getLocalParams</td><td>获取当前 form 的作用域数据信息.当 key 有值的时候将会获取指定的数据，若没有则进行获取作用域的所有数据;</td><td>key?: string</td><td>object</td></tr><tr><td>setData</td><td>以键值对的方式设置表单数据</td><td>key: string, value: any</td><td>this</td></tr><tr><td>setDataMap</td><td>批量设置表单数据</td><td>&#123; key: string,value: any &#125;[]</td><td>this</td></tr><tr><td>getParams</td><td>获取表单的数据包含有通过 setLocalParams/setLocalParamsMap 所设值的本地数据,默认返回表单的数据信息，当参数为 true 的是就是代表进行表单验证再获取结果并返回一个 Promise</td><td>bool?: Boolean</td><td>Object ｜ Promise</td></tr><tr><td>validateFields</td><td>表单效验</td><td>-</td><td>Promise</td></tr><tr><td>getFieldsValue</td><td>获取表单数据</td><td>&#123; key: string,value: any &#125;[]</td><td>this</td></tr><tr><td>setOptions</td><td>给指定的 prop 配置信息进行设置选项。普遍用在与 select/radio</td><td>prop: string,options: any[]</td><td>this</td></tr><tr><td>setOptionsMap</td><td>批量进行给指定的 prop 配置信息进行设置选项。普遍用在与 select/radio</td><td>&#123; [key: string]: any[] &#125;</td><td>this</td></tr><tr><td>setDisabled</td><td>给表单的每一项进行设置是否禁用效果。 当 props 有值的时候，则就是给指定的 prop 或者指定 prop 数组进行设置是否禁用效果,当 props 没有值的时候，则是代表全部 prop;</td><td>disabled: boolean, props?: string</td><td>string[]</td></tr><tr><td>getOptions</td><td>获取指定 prop 值的选项列表，当第二个参数 value 有值的时候则就是获取选项中指定 value 的选项信息</td><td>prop: string, value?: string</td><td>number</td></tr><tr><td>update</td><td>通过 prop 值进行更新指定的配置信息</td><td>prop: string, config: IConfigSignle</td><td>this</td></tr><tr><td>replace</td><td>替换指定 prop 值的配置信息</td><td>prop: string, config: IConfigSignle</td><td>this</td></tr><tr><td>delete</td><td>删除指定的 prop</td><td>prop: string</td><td>this</td></tr><tr><td>push</td><td>添加配置信息,该添加是直接在根级节点的配置信息上进行添加一个一行数组</td><td>config: IConfig</td><td>this</td></tr><tr><td>appendBefore</td><td>添加到指定 prop 字段前面</td><td>prop: string, config: IconfigSignle</td><td>this</td></tr><tr><td>appendAfter</td><td>添加到指定 prop 字段后面</td><td>prop: string, config: IconfigSignle</td><td>this</td></tr></tbody></table>
<h2 data-id="heading-9"><strong><em>Events</em></strong></h2>























<table><thead><tr><th>事件名</th><th>说明</th><th>参数</th><th>返回</th></tr></thead><tbody><tr><td>loaded</td><td>当动态表单加载完毕之后进行触发的</td><td>&#123;vm: 动态表单，formData: 表单信息&#125;</td><td>-</td></tr><tr><td>formHandler</td><td>当 events 配置有 method，并且$props.parentName 没有进行配置的时候进行触发</td><td>method:当前 events 的 method 值,&#123;value:当前 prop 的值,formData:表单数据,config:当前的 prop 的配置信息,args: 当前原函数的 argments&#125;</td><td>-</td></tr></tbody></table>
<h2 data-id="heading-10"><strong><em>ConfigSingle</em></strong></h2>





































































































<table><thead><tr><th>参数</th><th>说明</th><th>是否为必选项</th><th>类型</th></tr></thead><tbody><tr><td>label</td><td>表单 label</td><td>否</td><td>string</td></tr><tr><td>prop</td><td>数据的 key 名称，可为点连接的数据。例如：user.name</td><td>是</td><td>string</td></tr><tr><td>type</td><td>来源与 mapping.componentMapping 配置信息中的 key 名</td><td>是</td><td>string</td></tr><tr><td>bind</td><td>当前选中的组件的$props 参数</td><td>否</td><td>object</td></tr><tr><td>itemBind</td><td>当前组件的 form-item 的$props 参数</td><td>否</td><td>object</td></tr><tr><td>hideLabel</td><td>是否隐藏 label，当为 true 的时候则就会在相对应的项中添加'hideLabel'的 class 名称</td><td>否</td><td>boolean</td></tr><tr><td>span</td><td>所占当前父级宽度的空间，以 24 等份为基础进行计算对应的空间</td><td>否</td><td>number</td></tr><tr><td>required</td><td>是否为必填项</td><td>否</td><td>boolean</td></tr><tr><td>rules</td><td>单个 prop 的效验规则数组。同所用的 UI 框架一致。需要注意的是：里面自定义的 validator 函数的 this 指向是动态表单的 this</td><td>否</td><td>array</td></tr><tr><td>events</td><td>自定义事件处理函数</td><td>否</td><td>array</td></tr><tr><td>events[0].name</td><td>当前所选的组件所能触发的事件名称。当 name 值为 create 的时候，则就会在组件加载完毕后进行触发一次</td><td>是</td><td>string</td></tr><tr><td>events[0].hadnler</td><td>自定义函数，当前的函数的 this 指向是动态表单的 this</td><td>否</td><td>function</td></tr><tr><td>events[0].method</td><td>当前动态表单的父级节点的 method 函数。需要注意的是：必须配置$props.parentName</td><td>否</td><td>string</td></tr><tr><td>slots</td><td>自定义插槽</td><td>否</td><td>function</td></tr><tr><td>optionType</td><td>来源与 mapping.componentMapping 配置信息中的 key 名。主要使用来配合 select/raido 的选项列表</td><td>否</td><td>string</td></tr></tbody></table></div>  
</div>
            