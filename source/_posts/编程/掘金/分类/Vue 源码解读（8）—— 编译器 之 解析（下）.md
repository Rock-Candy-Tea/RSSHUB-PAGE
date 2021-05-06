
---
title: 'Vue 源码解读（8）—— 编译器 之 解析（下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5451'
author: 掘金
comments: false
date: Wed, 05 May 2021 19:51:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=5451'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">特殊说明</h1>
<p>由于文章篇幅限制，所以将 <a href="https://juejin.cn/post/6959019076983209992" target="_blank">Vue 源码解读（8）—— 编译器 之 解析</a> 拆成了两篇文章，本篇是对 <a href="https://juejin.cn/post/6959019076983209992" target="_blank">Vue 源码解读（8）—— 编译器 之 解析（上）</a> 的一个补充，所以在阅读时请同时打开 <a href="https://juejin.cn/post/6959019076983209992" target="_blank">Vue 源码解读（8）—— 编译器 之 解析（上）</a> 一起阅读。</p>
<h2 data-id="heading-1">processAttrs</h2>
<blockquote>
<p>/src/compiler/parser/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理元素上的所有属性：
 * v-bind 指令变成：el.attrs 或 el.dynamicAttrs = [&#123; name, value, start, end, dynamic &#125;, ...]，
 *                或者是必须使用 props 的属性，变成了 el.props = [&#123; name, value, start, end, dynamic &#125;, ...]
 * v-on 指令变成：el.events 或 el.nativeEvents = &#123; name: [&#123; value, start, end, modifiers, dynamic &#125;, ...] &#125;
 * 其它指令：el.directives = [&#123;name, rawName, value, arg, isDynamicArg, modifier, start, end &#125;, ...]
 * 原生属性：el.attrs = [&#123; name, value, start, end &#125;]，或者一些必须使用 props 的属性，变成了：
 *         el.props = [&#123; name, value: true, start, end, dynamic &#125;]
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processAttrs</span>(<span class="hljs-params">el</span>) </span>&#123;
  <span class="hljs-comment">// list = [&#123; name, value, start, end &#125;, ...]</span>
  <span class="hljs-keyword">const</span> list = el.attrsList
  <span class="hljs-keyword">let</span> i, l, name, rawName, value, modifiers, syncGen, isDynamic
  <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>, l = list.length; i < l; i++) &#123;
    <span class="hljs-comment">// 属性名</span>
    name = rawName = list[i].name
    <span class="hljs-comment">// 属性值</span>
    value = list[i].value
    <span class="hljs-keyword">if</span> (dirRE.test(name)) &#123;
      <span class="hljs-comment">// 说明该属性是一个指令</span>

      <span class="hljs-comment">// 元素上存在指令，将元素标记动态元素</span>
      <span class="hljs-comment">// mark element as dynamic</span>
      el.hasBindings = <span class="hljs-literal">true</span>
      <span class="hljs-comment">// modifiers，在属性名上解析修饰符，比如 xx.lazy</span>
      modifiers = parseModifiers(name.replace(dirRE, <span class="hljs-string">''</span>))
      <span class="hljs-comment">// support .foo shorthand syntax for the .prop modifier</span>
      <span class="hljs-keyword">if</span> (process.env.VBIND_PROP_SHORTHAND && propBindRE.test(name)) &#123;
        <span class="hljs-comment">// 为 .props 修饰符支持 .foo 速记写法</span>
        (modifiers || (modifiers = &#123;&#125;)).prop = <span class="hljs-literal">true</span>
        name = <span class="hljs-string">`.`</span> + name.slice(<span class="hljs-number">1</span>).replace(modifierRE, <span class="hljs-string">''</span>)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (modifiers) &#123;
        <span class="hljs-comment">// 属性中的修饰符去掉，得到一个干净的属性名</span>
        name = name.replace(modifierRE, <span class="hljs-string">''</span>)
      &#125;
      <span class="hljs-keyword">if</span> (bindRE.test(name)) &#123; <span class="hljs-comment">// v-bind, <div :id="test"></div></span>
        <span class="hljs-comment">// 处理 v-bind 指令属性，最后得到 el.attrs 或者 el.dynamicAttrs = [&#123; name, value, start, end, dynamic &#125;, ...]</span>

        <span class="hljs-comment">// 属性名，比如：id</span>
        name = name.replace(bindRE, <span class="hljs-string">''</span>)
        <span class="hljs-comment">// 属性值，比如：test</span>
        value = parseFilters(value)
        <span class="hljs-comment">// 是否为动态属性 <div :[id]="test"></div></span>
        isDynamic = dynamicArgRE.test(name)
        <span class="hljs-keyword">if</span> (isDynamic) &#123;
          <span class="hljs-comment">// 如果是动态属性，则去掉属性两侧的方括号 []</span>
          name = name.slice(<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>)
        &#125;
        <span class="hljs-comment">// 提示，动态属性值不能为空字符串</span>
        <span class="hljs-keyword">if</span> (
          process.env.NODE_ENV !== <span class="hljs-string">'production'</span> &&
          value.trim().length === <span class="hljs-number">0</span>
        ) &#123;
          warn(
            <span class="hljs-string">`The value for a v-bind expression cannot be empty. Found in "v-bind:<span class="hljs-subst">$&#123;name&#125;</span>"`</span>
          )
        &#125;
        <span class="hljs-comment">// 存在修饰符</span>
        <span class="hljs-keyword">if</span> (modifiers) &#123;
          <span class="hljs-keyword">if</span> (modifiers.prop && !isDynamic) &#123;
            name = camelize(name)
            <span class="hljs-keyword">if</span> (name === <span class="hljs-string">'innerHtml'</span>) name = <span class="hljs-string">'innerHTML'</span>
          &#125;
          <span class="hljs-keyword">if</span> (modifiers.camel && !isDynamic) &#123;
            name = camelize(name)
          &#125;
          <span class="hljs-comment">// 处理 sync 修饰符</span>
          <span class="hljs-keyword">if</span> (modifiers.sync) &#123;
            syncGen = genAssignmentCode(value, <span class="hljs-string">`$event`</span>)
            <span class="hljs-keyword">if</span> (!isDynamic) &#123;
              addHandler(
                el,
                <span class="hljs-string">`update:<span class="hljs-subst">$&#123;camelize(name)&#125;</span>`</span>,
                syncGen,
                <span class="hljs-literal">null</span>,
                <span class="hljs-literal">false</span>,
                warn,
                list[i]
              )
              <span class="hljs-keyword">if</span> (hyphenate(name) !== camelize(name)) &#123;
                addHandler(
                  el,
                  <span class="hljs-string">`update:<span class="hljs-subst">$&#123;hyphenate(name)&#125;</span>`</span>,
                  syncGen,
                  <span class="hljs-literal">null</span>,
                  <span class="hljs-literal">false</span>,
                  warn,
                  list[i]
                )
              &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
              <span class="hljs-comment">// handler w/ dynamic event name</span>
              addHandler(
                el,
                <span class="hljs-string">`"update:"+(<span class="hljs-subst">$&#123;name&#125;</span>)`</span>,
                syncGen,
                <span class="hljs-literal">null</span>,
                <span class="hljs-literal">false</span>,
                warn,
                list[i],
                <span class="hljs-literal">true</span> <span class="hljs-comment">// dynamic</span>
              )
            &#125;
          &#125;
        &#125;
        <span class="hljs-keyword">if</span> ((modifiers && modifiers.prop) || (
          !el.component && platformMustUseProp(el.tag, el.attrsMap.type, name)
        )) &#123;
          <span class="hljs-comment">// 将属性对象添加到 el.props 数组中，表示这些属性必须通过 props 设置</span>
          <span class="hljs-comment">// el.props = [&#123; name, value, start, end, dynamic &#125;, ...]</span>
          addProp(el, name, value, list[i], isDynamic)
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// 将属性添加到 el.attrs 数组或者 el.dynamicAttrs 数组</span>
          addAttr(el, name, value, list[i], isDynamic)
        &#125;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (onRE.test(name)) &#123; <span class="hljs-comment">// v-on, 处理事件，<div @click="test"></div></span>
        <span class="hljs-comment">// 属性名，即事件名</span>
        name = name.replace(onRE, <span class="hljs-string">''</span>)
        <span class="hljs-comment">// 是否为动态属性</span>
        isDynamic = dynamicArgRE.test(name)
        <span class="hljs-keyword">if</span> (isDynamic) &#123;
          <span class="hljs-comment">// 动态属性，则获取 [] 中的属性名</span>
          name = name.slice(<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>)
        &#125;
        <span class="hljs-comment">// 处理事件属性，将属性的信息添加到 el.events 或者 el.nativeEvents 对象上，格式：</span>
        <span class="hljs-comment">// el.events = [&#123; value, start, end, modifiers, dynamic &#125;, ...]</span>
        addHandler(el, name, value, modifiers, <span class="hljs-literal">false</span>, warn, list[i], isDynamic)
      &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// normal directives，其它的普通指令</span>
        <span class="hljs-comment">// 得到 el.directives = [&#123;name, rawName, value, arg, isDynamicArg, modifier, start, end &#125;, ...]</span>
        name = name.replace(dirRE, <span class="hljs-string">''</span>)
        <span class="hljs-comment">// parse arg</span>
        <span class="hljs-keyword">const</span> argMatch = name.match(argRE)
        <span class="hljs-keyword">let</span> arg = argMatch && argMatch[<span class="hljs-number">1</span>]
        isDynamic = <span class="hljs-literal">false</span>
        <span class="hljs-keyword">if</span> (arg) &#123;
          name = name.slice(<span class="hljs-number">0</span>, -(arg.length + <span class="hljs-number">1</span>))
          <span class="hljs-keyword">if</span> (dynamicArgRE.test(arg)) &#123;
            arg = arg.slice(<span class="hljs-number">1</span>, -<span class="hljs-number">1</span>)
            isDynamic = <span class="hljs-literal">true</span>
          &#125;
        &#125;
        addDirective(el, name, rawName, value, arg, isDynamic, modifiers, list[i])
        <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && name === <span class="hljs-string">'model'</span>) &#123;
          checkForAliasModel(el, value)
        &#125;
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 当前属性不是指令</span>
      <span class="hljs-comment">// literal attribute</span>
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
        <span class="hljs-keyword">const</span> res = parseText(value, delimiters)
        <span class="hljs-keyword">if</span> (res) &#123;
          warn(
            <span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>="<span class="hljs-subst">$&#123;value&#125;</span>": `</span> +
            <span class="hljs-string">'Interpolation inside attributes has been removed. '</span> +
            <span class="hljs-string">'Use v-bind or the colon shorthand instead. For example, '</span> +
            <span class="hljs-string">'instead of <div id="&#123;&#123; val &#125;&#125;">, use <div :id="val">.'</span>,
            list[i]
          )
        &#125;
      &#125;
      <span class="hljs-comment">// 将属性对象放到 el.attrs 数组中，el.attrs = [&#123; name, value, start, end &#125;]</span>
      addAttr(el, name, <span class="hljs-built_in">JSON</span>.stringify(value), list[i])
      <span class="hljs-comment">// #6887 firefox doesn't update muted state if set via attribute</span>
      <span class="hljs-comment">// even immediately after element creation</span>
      <span class="hljs-keyword">if</span> (!el.component &&
        name === <span class="hljs-string">'muted'</span> &&
        platformMustUseProp(el.tag, el.attrsMap.type, name)) &#123;
        addProp(el, name, <span class="hljs-string">'true'</span>, list[i])
      &#125;
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">addHandler</h2>
<blockquote>
<p>/src/compiler/helpers.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理事件属性，将事件属性添加到 el.events 对象或者 el.nativeEvents 对象中，格式：
 * el.events[name] = [&#123; value, start, end, modifiers, dynamic &#125;, ...]
 * 其中用了大量的篇幅在处理 name 属性带修饰符 (modifier) 的情况
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>el ast 对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>name 属性名，即事件名
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>value 属性值，即事件回调函数名
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>modifiers 修饰符
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>important 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>warn 日志
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>range 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>dynamic 属性名是否为动态属性
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addHandler</span> (<span class="hljs-params">
  el: ASTElement,
  name: string,
  value: string,
  modifiers: ?ASTModifiers,
  important?: boolean,
  warn?: ?<span class="hljs-built_in">Function</span>,
  range?: Range,
  dynamic?: boolean
</span>) </span>&#123;
  <span class="hljs-comment">// modifiers 是一个对象，如果传递的参数为空，则给一个冻结的空对象</span>
  modifiers = modifiers || emptyObject
  <span class="hljs-comment">// 提示：prevent 和 passive 修饰符不能一起使用</span>
  <span class="hljs-comment">// warn prevent and passive modifier</span>
  <span class="hljs-comment">/* istanbul ignore if */</span>
  <span class="hljs-keyword">if</span> (
    process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && warn &&
    modifiers.prevent && modifiers.passive
  ) &#123;
    warn(
      <span class="hljs-string">'passive and prevent can\'t be used together. '</span> +
      <span class="hljs-string">'Passive handler can\'t prevent default event.'</span>,
      range
    )
  &#125;

  <span class="hljs-comment">// 标准化 click.right 和 click.middle，它们实际上不会被真正的触发，从技术讲他们是它们</span>
  <span class="hljs-comment">// 是特定于浏览器的，但至少目前位置只有浏览器才具有右键和中间键的点击</span>
  <span class="hljs-comment">// normalize click.right and click.middle since they don't actually fire</span>
  <span class="hljs-comment">// this is technically browser-specific, but at least for now browsers are</span>
  <span class="hljs-comment">// the only target envs that have right/middle clicks.</span>
  <span class="hljs-keyword">if</span> (modifiers.right) &#123;
    <span class="hljs-comment">// 右键</span>
    <span class="hljs-keyword">if</span> (dynamic) &#123;
      <span class="hljs-comment">// 动态属性</span>
      name = <span class="hljs-string">`(<span class="hljs-subst">$&#123;name&#125;</span>)==='click'?'contextmenu':(<span class="hljs-subst">$&#123;name&#125;</span>)`</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (name === <span class="hljs-string">'click'</span>) &#123;
      <span class="hljs-comment">// 非动态属性，name = contextmenu</span>
      name = <span class="hljs-string">'contextmenu'</span>
      <span class="hljs-comment">// 删除修饰符中的 right 属性</span>
      <span class="hljs-keyword">delete</span> modifiers.right
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (modifiers.middle) &#123;
    <span class="hljs-comment">// 中间键</span>
    <span class="hljs-keyword">if</span> (dynamic) &#123;
      <span class="hljs-comment">// 动态属性，name => mouseup 或者 $&#123;name&#125;</span>
      name = <span class="hljs-string">`(<span class="hljs-subst">$&#123;name&#125;</span>)==='click'?'mouseup':(<span class="hljs-subst">$&#123;name&#125;</span>)`</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (name === <span class="hljs-string">'click'</span>) &#123;
      <span class="hljs-comment">// 非动态属性，mouseup</span>
      name = <span class="hljs-string">'mouseup'</span>
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * 处理 capture、once、passive 这三个修饰符，通过给 name 添加不同的标记来标记这些修饰符
   */</span>
  <span class="hljs-comment">// check capture modifier</span>
  <span class="hljs-keyword">if</span> (modifiers.capture) &#123;
    <span class="hljs-keyword">delete</span> modifiers.capture
    <span class="hljs-comment">// 给带有 capture 修饰符的属性，加上 ! 标记</span>
    name = prependModifierMarker(<span class="hljs-string">'!'</span>, name, dynamic)
  &#125;
  <span class="hljs-keyword">if</span> (modifiers.once) &#123;
    <span class="hljs-keyword">delete</span> modifiers.once
    <span class="hljs-comment">// once 修饰符加 ~ 标记</span>
    name = prependModifierMarker(<span class="hljs-string">'~'</span>, name, dynamic)
  &#125;
  <span class="hljs-comment">/* istanbul ignore if */</span>
  <span class="hljs-keyword">if</span> (modifiers.passive) &#123;
    <span class="hljs-keyword">delete</span> modifiers.passive
    <span class="hljs-comment">// passive 修饰符加 & 标记</span>
    name = prependModifierMarker(<span class="hljs-string">'&'</span>, name, dynamic)
  &#125;

  <span class="hljs-keyword">let</span> events
  <span class="hljs-keyword">if</span> (modifiers.native) &#123;
    <span class="hljs-comment">// native 修饰符， 监听组件根元素的原生事件，将事件信息存放到 el.nativeEvents 对象中</span>
    <span class="hljs-keyword">delete</span> modifiers.native
    events = el.nativeEvents || (el.nativeEvents = &#123;&#125;)
  &#125; <span class="hljs-keyword">else</span> &#123;
    events = el.events || (el.events = &#123;&#125;)
  &#125;

  <span class="hljs-keyword">const</span> newHandler: any = rangeSetItem(&#123; <span class="hljs-attr">value</span>: value.trim(), dynamic &#125;, range)
  <span class="hljs-keyword">if</span> (modifiers !== emptyObject) &#123;
    <span class="hljs-comment">// 说明有修饰符，将修饰符对象放到 newHandler 对象上</span>
    <span class="hljs-comment">// &#123; value, dynamic, start, end, modifiers &#125;</span>
    newHandler.modifiers = modifiers
  &#125;

  <span class="hljs-comment">// 将配置对象放到 events[name] = [newHander, handler, ...]</span>
  <span class="hljs-keyword">const</span> handlers = events[name]
  <span class="hljs-comment">/* istanbul ignore if */</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(handlers)) &#123;
    important ? handlers.unshift(newHandler) : handlers.push(newHandler)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (handlers) &#123;
    events[name] = important ? [newHandler, handlers] : [handlers, newHandler]
  &#125; <span class="hljs-keyword">else</span> &#123;
    events[name] = newHandler
  &#125;

  el.plain = <span class="hljs-literal">false</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">addIfCondition</h2>
<blockquote>
<p>/src/compiler/parser/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 将传递进来的条件对象放进 el.ifConditions 数组中
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addIfCondition</span>(<span class="hljs-params">el: ASTElement, condition: ASTIfCondition</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!el.ifConditions) &#123;
    el.ifConditions = []
  &#125;
  el.ifConditions.push(condition)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">processPre</h2>
<blockquote>
<p>/src/compiler/parser/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 如果元素上存在 v-pre 指令，则设置 el.pre = true 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processPre</span>(<span class="hljs-params">el</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (getAndRemoveAttr(el, <span class="hljs-string">'v-pre'</span>) != <span class="hljs-literal">null</span>) &#123;
    el.pre = <span class="hljs-literal">true</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">processRawAttrs</h2>
<blockquote>
<p>/src/compiler/parser/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 设置 el.attrs 数组对象，每个元素都是一个属性对象 &#123; name: attrName, value: attrVal, start, end &#125;
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processRawAttrs</span>(<span class="hljs-params">el</span>) </span>&#123;
  <span class="hljs-keyword">const</span> list = el.attrsList
  <span class="hljs-keyword">const</span> len = list.length
  <span class="hljs-keyword">if</span> (len) &#123;
    <span class="hljs-keyword">const</span> attrs: <span class="hljs-built_in">Array</span><ASTAttr> = el.attrs = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(len)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
      attrs[i] = &#123;
        <span class="hljs-attr">name</span>: list[i].name,
        <span class="hljs-attr">value</span>: <span class="hljs-built_in">JSON</span>.stringify(list[i].value)
      &#125;
      <span class="hljs-keyword">if</span> (list[i].start != <span class="hljs-literal">null</span>) &#123;
        attrs[i].start = list[i].start
        attrs[i].end = list[i].end
      &#125;
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!el.pre) &#123;
    <span class="hljs-comment">// non root node in pre blocks with no attributes</span>
    el.plain = <span class="hljs-literal">true</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">processIf</h2>
<blockquote>
<p>/src/compiler/parser/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理 v-if、v-else-if、v-else
 * 得到 el.if = "exp"，el.elseif = exp, el.else = true
 * v-if 属性会额外在 el.ifConditions 数组中添加 &#123; exp, block &#125; 对象
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processIf</span>(<span class="hljs-params">el</span>) </span>&#123;
  <span class="hljs-comment">// 获取 v-if 属性的值，比如 <div v-if="test"></div></span>
  <span class="hljs-keyword">const</span> exp = getAndRemoveAttr(el, <span class="hljs-string">'v-if'</span>)
  <span class="hljs-keyword">if</span> (exp) &#123;
    <span class="hljs-comment">// el.if = "test"</span>
    el.if = exp
    <span class="hljs-comment">// 在 el.ifConditions 数组中添加 &#123; exp, block &#125;</span>
    addIfCondition(el, &#123;
      <span class="hljs-attr">exp</span>: exp,
      <span class="hljs-attr">block</span>: el
    &#125;)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 处理 v-else，得到 el.else = true</span>
    <span class="hljs-keyword">if</span> (getAndRemoveAttr(el, <span class="hljs-string">'v-else'</span>) != <span class="hljs-literal">null</span>) &#123;
      el.else = <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-comment">// 处理 v-else-if，得到 el.elseif = exp</span>
    <span class="hljs-keyword">const</span> elseif = getAndRemoveAttr(el, <span class="hljs-string">'v-else-if'</span>)
    <span class="hljs-keyword">if</span> (elseif) &#123;
      el.elseif = elseif
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">processOnce</h2>
<blockquote>
<p>/src/compiler/parser/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 处理 v-once 指令，得到 el.once = true
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>el 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processOnce</span>(<span class="hljs-params">el</span>) </span>&#123;
  <span class="hljs-keyword">const</span> once = getAndRemoveAttr(el, <span class="hljs-string">'v-once'</span>)
  <span class="hljs-keyword">if</span> (once != <span class="hljs-literal">null</span>) &#123;
    el.once = <span class="hljs-literal">true</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">checkRootConstraints</h2>
<blockquote>
<p>/src/compiler/parser/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 检查根元素：
 *   不能使用 slot 和 template 标签作为组件的根元素
 *   不能在有状态组件的 根元素 上使用 v-for 指令，因为它会渲染出多个元素
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>el 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkRootConstraints</span>(<span class="hljs-params">el</span>) </span>&#123;
  <span class="hljs-comment">// 不能使用 slot 和 template 标签作为组件的根元素</span>
  <span class="hljs-keyword">if</span> (el.tag === <span class="hljs-string">'slot'</span> || el.tag === <span class="hljs-string">'template'</span>) &#123;
    warnOnce(
      <span class="hljs-string">`Cannot use <<span class="hljs-subst">$&#123;el.tag&#125;</span>> as component root element because it may `</span> +
      <span class="hljs-string">'contain multiple nodes.'</span>,
      &#123; <span class="hljs-attr">start</span>: el.start &#125;
    )
  &#125;
  <span class="hljs-comment">// 不能在有状态组件的 根元素 上使用 v-for，因为它会渲染出多个元素</span>
  <span class="hljs-keyword">if</span> (el.attrsMap.hasOwnProperty(<span class="hljs-string">'v-for'</span>)) &#123;
    warnOnce(
      <span class="hljs-string">'Cannot use v-for on stateful component root element because '</span> +
      <span class="hljs-string">'it renders multiple elements.'</span>,
      el.rawAttrsMap[<span class="hljs-string">'v-for'</span>]
    )
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">closeElement</h2>
<blockquote>
<p>/src/compiler/parser/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 主要做了 3 件事：
 *   1、如果元素没有被处理过，即 el.processed 为 false，则调用 processElement 方法处理节点上的众多属性
 *   2、让自己和父元素产生关系，将自己放到父元素的 children 数组中，并设置自己的 parent 属性为 currentParent
 *   3、设置自己的子元素，将自己所有非插槽的子元素放到自己的 children 数组中
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">closeElement</span>(<span class="hljs-params">element</span>) </span>&#123;
  <span class="hljs-comment">// 移除节点末尾的空格，当前 pre 标签内的元素除外</span>
  trimEndingWhitespace(element)
  <span class="hljs-comment">// 当前元素不再 pre 节点内，并且也没有被处理过</span>
  <span class="hljs-keyword">if</span> (!inVPre && !element.processed) &#123;
    <span class="hljs-comment">// 分别处理元素节点的 key、ref、插槽、自闭合的 slot 标签、动态组件、class、style、v-bind、v-on、其它指令和一些原生属性 </span>
    element = processElement(element, options)
  &#125;
  <span class="hljs-comment">// 处理根节点上存在 v-if、v-else-if、v-else 指令的情况</span>
  <span class="hljs-comment">// 如果根节点存在 v-if 指令，则必须还提供一个具有 v-else-if 或者 v-else 的同级别节点，防止根元素不存在</span>
  <span class="hljs-comment">// tree management</span>
  <span class="hljs-keyword">if</span> (!stack.length && element !== root) &#123;
    <span class="hljs-comment">// allow root elements with v-if, v-else-if and v-else</span>
    <span class="hljs-keyword">if</span> (root.if && (element.elseif || element.else)) &#123;
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
        <span class="hljs-comment">// 检查根元素</span>
        checkRootConstraints(element)
      &#125;
      <span class="hljs-comment">// 给根元素设置 ifConditions 属性，root.ifConditions = [&#123; exp: element.elseif, block: element &#125;, ...]</span>
      addIfCondition(root, &#123;
        <span class="hljs-attr">exp</span>: element.elseif,
        <span class="hljs-attr">block</span>: element
      &#125;)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
      <span class="hljs-comment">// 提示，表示不应该在 根元素 上只使用 v-if，应该将 v-if、v-else-if 一起使用，保证组件只有一个根元素</span>
      warnOnce(
        <span class="hljs-string">`Component template should contain exactly one root element. `</span> +
        <span class="hljs-string">`If you are using v-if on multiple elements, `</span> +
        <span class="hljs-string">`use v-else-if to chain them instead.`</span>,
        &#123; <span class="hljs-attr">start</span>: element.start &#125;
      )
    &#125;
  &#125;
  <span class="hljs-comment">// 让自己和父元素产生关系</span>
  <span class="hljs-comment">// 将自己放到父元素的 children 数组中，然后设置自己的 parent 属性为 currentParent</span>
  <span class="hljs-keyword">if</span> (currentParent && !element.forbidden) &#123;
    <span class="hljs-keyword">if</span> (element.elseif || element.else) &#123;
      processIfConditions(element, currentParent)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">if</span> (element.slotScope) &#123;
        <span class="hljs-comment">// scoped slot</span>
        <span class="hljs-comment">// keep it in the children list so that v-else(-if) conditions can</span>
        <span class="hljs-comment">// find it as the prev node.</span>
        <span class="hljs-keyword">const</span> name = element.slotTarget || <span class="hljs-string">'"default"'</span>
          ; (currentParent.scopedSlots || (currentParent.scopedSlots = &#123;&#125;))[name] = element
      &#125;
      currentParent.children.push(element)
      element.parent = currentParent
    &#125;
  &#125;

  <span class="hljs-comment">// 设置自己的子元素</span>
  <span class="hljs-comment">// 将自己的所有非插槽的子元素设置到 element.children 数组中</span>
  <span class="hljs-comment">// final children cleanup</span>
  <span class="hljs-comment">// filter out scoped slots</span>
  element.children = element.children.filter(<span class="hljs-function"><span class="hljs-params">c</span> =></span> !(c: any).slotScope)
  <span class="hljs-comment">// remove trailing whitespace node again</span>
  trimEndingWhitespace(element)

  <span class="hljs-comment">// check pre state</span>
  <span class="hljs-keyword">if</span> (element.pre) &#123;
    inVPre = <span class="hljs-literal">false</span>
  &#125;
  <span class="hljs-keyword">if</span> (platformIsPreTag(element.tag)) &#123;
    inPre = <span class="hljs-literal">false</span>
  &#125;
  <span class="hljs-comment">// 分别为 element 执行 model、class、style 三个模块的 postTransform 方法</span>
  <span class="hljs-comment">// 但是 web 平台没有提供该方法</span>
  <span class="hljs-comment">// apply post-transforms</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < postTransforms.length; i++) &#123;
    postTransforms[i](element, options)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">trimEndingWhitespace</h2>
<blockquote>
<p>/src/compiler/parser/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 删除元素中空白的文本节点，比如：<div> </div>，删除 div 元素中的空白节点，将其从元素的 children 属性中移出去
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trimEndingWhitespace</span>(<span class="hljs-params">el</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!inPre) &#123;
    <span class="hljs-keyword">let</span> lastNode
    <span class="hljs-keyword">while</span> (
      (lastNode = el.children[el.children.length - <span class="hljs-number">1</span>]) &&
      lastNode.type === <span class="hljs-number">3</span> &&
      lastNode.text === <span class="hljs-string">' '</span>
    ) &#123;
      el.children.pop()
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">processIfConditions</h2>
<blockquote>
<p>/src/compiler/parser/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processIfConditions</span>(<span class="hljs-params">el, parent</span>) </span>&#123;
  <span class="hljs-comment">// 找到 parent.children 中的最后一个元素节点</span>
  <span class="hljs-keyword">const</span> prev = findPrevElement(parent.children)
  <span class="hljs-keyword">if</span> (prev && prev.if) &#123;
    addIfCondition(prev, &#123;
      <span class="hljs-attr">exp</span>: el.elseif,
      <span class="hljs-attr">block</span>: el
    &#125;)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
    warn(
      <span class="hljs-string">`v-<span class="hljs-subst">$&#123;el.elseif ? (<span class="hljs-string">'else-if="'</span> + el.elseif + <span class="hljs-string">'"'</span>) : <span class="hljs-string">'else'</span>&#125;</span> `</span> +
      <span class="hljs-string">`used on element <<span class="hljs-subst">$&#123;el.tag&#125;</span>> without corresponding v-if.`</span>,
      el.rawAttrsMap[el.elseif ? <span class="hljs-string">'v-else-if'</span> : <span class="hljs-string">'v-else'</span>]
    )
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">findPrevElement</h2>
<blockquote>
<p>/src/compiler/parser/index.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 找到 children 中的最后一个元素节点 
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">findPrevElement</span>(<span class="hljs-params">children: <span class="hljs-built_in">Array</span><any></span>): <span class="hljs-title">ASTElement</span> | <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">let</span> i = children.length
  <span class="hljs-keyword">while</span> (i--) &#123;
    <span class="hljs-keyword">if</span> (children[i].type === <span class="hljs-number">1</span>) &#123;
      <span class="hljs-keyword">return</span> children[i]
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && children[i].text !== <span class="hljs-string">' '</span>) &#123;
        warn(
          <span class="hljs-string">`text "<span class="hljs-subst">$&#123;children[i].text.trim()&#125;</span>" between v-if and v-else(-if) `</span> +
          <span class="hljs-string">`will be ignored.`</span>,
          children[i]
        )
      &#125;
      children.pop()
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">帮助</h1>
<p>到这里编译器的解析部分就结束了，相信很多人看的是云里雾里的，即使多看几遍可能也没有那么清晰。</p>
<p>不要着急，这个很正常，编译器这块儿的代码量确实是比较大。但是内容本身其实不复杂，复杂的是它要处理东西实在是太多了，这才导致这部分的代码量巨大，相对应的，就会产生比较难的感觉。确实不简单，至少我觉得它是整个框架最复杂最难的地方了。</p>
<p>对照着视频和文章大家可以多看几遍，不明白的地方写一些示例代码辅助调试，编写详细的注释。还是那句话，书读百遍，其义自现。</p>
<p>阅读的过程中，大家需要抓住编译器解析部分的本质：将类 HTML 字符串模版解析成 AST 对象。</p>
<p>所以这么多代码都在做一件事情，就是解析字符串模版，将整个模版用 AST 对象来表示和记录。所以，大家阅读的时候，可以将解析过程中生成的 AST 对象记录下来，帮助阅读和理解，这样在读完以后不至于那么迷茫，也有助于大家理解。</p>
<p>这是我在阅读的时候的一个简单记录：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> element = &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-number">1</span>,
  tag,
  <span class="hljs-attr">attrsList</span>: [&#123; <span class="hljs-attr">name</span>: attrName, <span class="hljs-attr">value</span>: attrVal, start, end &#125;],
  <span class="hljs-attr">attrsMap</span>: &#123; <span class="hljs-attr">attrName</span>: attrVal, &#125;,
  <span class="hljs-attr">rawAttrsMap</span>: &#123; <span class="hljs-attr">attrName</span>: attrVal, <span class="hljs-attr">type</span>: checkbox &#125;,
  <span class="hljs-comment">// v-if</span>
  <span class="hljs-attr">ifConditions</span>: [&#123; exp, block &#125;],
  <span class="hljs-comment">// v-for</span>
  <span class="hljs-attr">for</span>: iterator,
  <span class="hljs-attr">alias</span>: 别名,
  <span class="hljs-comment">// :key</span>
  <span class="hljs-attr">key</span>: xx,
  <span class="hljs-comment">// ref</span>
  <span class="hljs-attr">ref</span>: xx,
  <span class="hljs-attr">refInFor</span>: boolean,
  <span class="hljs-comment">// 插槽</span>
  <span class="hljs-attr">slotTarget</span>: slotName,
  <span class="hljs-attr">slotTargetDynamic</span>: boolean,
  <span class="hljs-attr">slotScope</span>: 作用域插槽的表达式,
  <span class="hljs-attr">scopeSlot</span>: &#123;
    <span class="hljs-attr">name</span>: &#123;
      <span class="hljs-attr">slotTarget</span>: slotName,
      <span class="hljs-attr">slotTargetDynamic</span>: boolean,
      <span class="hljs-attr">children</span>: &#123;
        <span class="hljs-attr">parent</span>: container,
        otherProperty,
      &#125;
    &#125;,
    <span class="hljs-attr">slotScope</span>: 作用域插槽的表达式,
  &#125;,
  <span class="hljs-attr">slotName</span>: xx,
  <span class="hljs-comment">// 动态组件</span>
  <span class="hljs-attr">component</span>: compName,
  <span class="hljs-attr">inlineTemplate</span>: boolean,
  <span class="hljs-comment">// class</span>
  <span class="hljs-attr">staticClass</span>: className,
  <span class="hljs-attr">classBinding</span>: xx,
  <span class="hljs-comment">// style</span>
  <span class="hljs-attr">staticStyle</span>: xx,
  <span class="hljs-attr">styleBinding</span>: xx,
  <span class="hljs-comment">// attr</span>
  <span class="hljs-attr">hasBindings</span>: boolean,
  <span class="hljs-attr">nativeEvents</span>: &#123;同 evetns&#125;,
  <span class="hljs-attr">events</span>: &#123;
    <span class="hljs-attr">name</span>: [&#123; value, dynamic, start, end, modifiers &#125;]
  &#125;,
  <span class="hljs-attr">props</span>: [&#123; name, value, dynamic, start, end &#125;],
  <span class="hljs-attr">dynamicAttrs</span>: [同 attrs],
  <span class="hljs-attr">attrs</span>: [&#123; name, value, dynamic, start, end &#125;],
  <span class="hljs-attr">directives</span>: [&#123; name, rawName, value, arg, isDynamicArg, modifiers, start, end &#125;],
  <span class="hljs-comment">// v-pre</span>
  <span class="hljs-attr">pre</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// v-once</span>
  <span class="hljs-attr">once</span>: <span class="hljs-literal">true</span>,
  parent,
  <span class="hljs-attr">children</span>: [],
  <span class="hljs-attr">plain</span>: boolean,
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">总结</h1>
<ul>
<li>
<p><strong>面试官 问</strong>：简单说一下 Vue 的编译器都做了什么？</p>
<p><strong>答</strong>：</p>
<p>Vue 的编译器做了三件事情：</p>
<ul>
<li>
<p>将组件的 html 模版解析成 AST 对象</p>
</li>
<li>
<p>优化，遍历 AST，为每个节点做静态标记，标记其是否为静态节点，然后进一步标记出静态根节点，这样在后续更新的过程中就可以跳过这些静态节点了；标记静态根用于生成渲染函数阶段，生成静态根节点的渲染函数</p>
</li>
<li>
<p>从 AST 生成运行时的渲染函数，即大家说的 render，其实还有一个，就是 staticRenderFns 数组，里面存放了所有的静态节点的渲染函数</p>
</li>
</ul>
</li>
</ul>
<hr>
<ul>
<li>
<p><strong>面试官 问</strong>：详细说一说编译器的解析过程，它是怎么将 html 字符串模版变成 AST 对象的？</p>
<p><strong>答</strong>：</p>
<ul>
<li>
<p>遍历 HTML 模版字符串，通过正则表达式匹配 "<"</p>
</li>
<li>
<p>跳过某些不需要处理的标签，比如：注释标签、条件注释标签、Doctype。</p>
<blockquote>
<p>备注：整个解析过程的核心是处理开始标签和结束标签</p>
</blockquote>
</li>
<li>
<p>解析开始标签</p>
<ul>
<li>
<p>得到一个对象，包括 标签名（tagName）、所有的属性（attrs）、标签在 html 模版字符串中的索引位置</p>
</li>
<li>
<p>进一步处理上一步得到的 attrs 属性，将其变成 [&#123; name: attrName, value: attrVal, start: xx, end: xx &#125;, ...] 的形式</p>
</li>
<li>
<p>通过标签名、属性对象和当前元素的父元素生成 AST 对象，其实就是一个 普通的 JS 对象，通过 key、value 的形式记录了该元素的一些信息</p>
</li>
<li>
<p>接下来进一步处理开始标签上的一些指令，比如 v-pre、v-for、v-if、v-once，并将处理结果放到 AST 对象上</p>
</li>
<li>
<p>处理结束将 ast 对象存放到 stack 数组</p>
</li>
<li>
<p>处理完成后会截断 html 字符串，将已经处理掉的字符串截掉</p>
</li>
</ul>
</li>
<li>
<p>解析闭合标签</p>
<ul>
<li>
<p>如果匹配到结束标签，就从 stack 数组中拿出最后一个元素，它和当前匹配到的结束标签是一对。</p>
</li>
<li>
<p>再次处理开始标签上的属性，这些属性和前面处理的不一样，比如：key、ref、scopedSlot、样式等，并将处理结果放到元素的 AST 对象上</p>
<blockquote>
<p><strong>备注</strong> 视频中说这块儿有误，回头看了下，没有问题，不需要改，确实是这样</p>
</blockquote>
</li>
<li>
<p>然后将当前元素和父元素产生联系，给当前元素的 ast 对象设置 parent 属性，然后将自己放到父元素的 ast 对象的 children 数组中</p>
</li>
</ul>
</li>
<li>
<p>最后遍历完整个 html 模版字符串以后，返回 ast 对象</p>
</li>
</ul>
</li>
</ul>
<h1 data-id="heading-15">配套视频</h1>
<p><a href="https://www.bilibili.com/video/BV1R54y1j7vM?share_source=copy_web" target="_blank" rel="nofollow noopener noreferrer">Vue 源码解读（8）—— 编译器 之 解析</a></p>
<h1 data-id="heading-16">求关注</h1>
<p>欢迎大家关注我的 <a href="https://juejin.cn/user/1028798616461326" target="_blank">掘金账号</a> 和 <a href="https://space.bilibili.com/359669053" target="_blank" rel="nofollow noopener noreferrer">B站</a>，如果内容有帮到你，欢迎大家点赞、收藏 + 关注</p>
<h1 data-id="heading-17">链接</h1>
<ul>
<li>
<p><a href="https://juejin.cn/post/6949370458793836580" target="_blank">Vue 源码解读（1）—— 前言</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6950084496515399717" target="_blank">Vue 源码解读（2）—— Vue 初始化过程</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6950826293923414047" target="_blank">Vue 源码解读（3）—— 响应式原理</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6951568091893465102" target="_blank">Vue 源码解读（4）—— 异步更新</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6952643167715852319" target="_blank">Vue 源码解读（5）—— 全局 API</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6953503236254859294" target="_blank">Vue 源码解读（6）—— 实例方法</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6954923081462710309" target="_blank">Vue 源码解读（7）—— Hook Event</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6959019076983209992" target="_blank">Vue 源码解读（8）—— 编译器 之 解析</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6959019174215548935">Vue 源码解读（9）—— 编译器 之 优化</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6959019174215548935">Vue 源码解读（10）—— 编译器 之 生成渲染函数</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6959019174215548935">Vue 源码解读（11）—— render helper</a></p>
</li>
</ul>
<h1 data-id="heading-18">学习交流群</h1>
<p><a href="https://juejin.cn/pin/6958238190398341134" target="_blank">链接</a></p></div>  
</div>
            