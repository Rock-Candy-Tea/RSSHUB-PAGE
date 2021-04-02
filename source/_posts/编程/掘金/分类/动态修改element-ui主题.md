
---
title: '动态修改element-ui主题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4856'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 01:55:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=4856'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://chasejourney.top/chJouBlog/" target="_blank" rel="nofollow noopener noreferrer">更多文章</a></p>
<h2 data-id="heading-0">前言</h2>
<p>ui库搭建的差不多了，接下来就是做组件的时候了，这里先做一个动态修改<code>element-ui</code>颜色的组件库</p>
<h2 data-id="heading-1">分析</h2>
<p><code>element-ui</code>提供了一个修改主题的方式（网上资料很多，这里不再赘述），就是修改<code>scss</code>变量，但这个是静态的，也就是你在代码运行前需要将这些配置都完成才能生效，项目启动成功后，我们加载的就是编译压缩后的<code>css</code>文件，如果要动态修改主题的话，通常做法就是生成一份新的样式，然后生成新的<code>style</code>标签并加入<code>DOM</code>中，覆盖之前的样式</p>
<h2 data-id="heading-2">实现</h2>
<p>接收一个初始化主题色的参数<code>defaultColor</code></p>
<pre><code class="hljs language-js copyable" lang="js">props: &#123;
    <span class="hljs-attr">defaultColor</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为保障<code>element-ui</code>的<code>css</code>版本的正确，我们从<code>element-ui/package.json</code>中读取版本</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> version = <span class="hljs-built_in">require</span>(<span class="hljs-string">"element-ui/package.json"</span>).version; <span class="hljs-comment">// 版本号</span>
<span class="hljs-keyword">const</span> url = <span class="hljs-string">`https://unpkg.com/element-ui@<span class="hljs-subst">$&#123;version&#125;</span>/lib/theme-chalk/index.css`</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即使访问<code>CDN</code>也仍有可能有网络的问题，所以我们也接受动态传入<code>url</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 默认访问CDN资源</span>
<span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">url</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: url
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即使动态改变主题，刷新后颜色亦会重置，所以我们接收一个<code>isCache</code>入参，决定是否缓存，缓存方案采用<code>localStorage</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 默认不缓存</span>
<span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">isCache</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来的主要逻辑(看代码吧)：</p>
<ol>
<li>调用<code>getThemeCluster</code>获取新旧心裂颜色</li>
<li>首次进入判断<code>this.chalk</code>是否已经缓存样式表内容，没有则调用<code>getCSSString</code>方法获取样式</li>
<li>调用<code>updateStyle</code>更新并获取最新的样式表内容</li>
<li>判断是否存在<code>id</code>为<code>chalk-style</code>的<code>style</code>的标签，没有则生成，有则赋值最新的样式表并加入<code>DOM</code></li>
</ol>
<h2 data-id="heading-3">完整代码</h2>
<pre><code class="hljs language-vue copyable" lang="vue">
<template>
  <el-color-picker
    :size="size"
    v-model="theme"
    class="theme-picker"
    @change="onChange"
    :predefine="predefineColors"
    popper-class="theme-picker-dropdown"
  >
  </el-color-picker>
</template>
 
<script>
const version = require("element-ui/package.json").version; // 版本号
const url = `https://unpkg.com/element-ui@$&#123;version&#125;/lib/theme-chalk/index.css`;
const ORIGINAL_THEME = "#409EFF";

export default &#123;
  name: "QjdTheme",
  data() &#123;
    return &#123;
      chalk: "",
      theme: "",
      predefineColors: Object.freeze([
        "#409EFF",
        "#ff4500",
        "#ff8c00",
        "#ffd700",
        "#90ee90",
        "#00ced1",
        "#1e90ff",
        "#c71585",
        "rgba(255, 69, 0, 0.68)",
        "rgb(255, 120, 0)",
        "hsv(51, 100, 98)",
        "hsva(120, 40, 94, 0.5)",
        "hsl(181, 100%, 37%)",
        "hsla(209, 100%, 56%, 0.73)",
        "#c7158577",
      ]),
    &#125;;
  &#125;,
  props: &#123;
    size: &#123;
      type: String,
      default() &#123;
        return "";
      &#125;,
    &#125;,
    defaultColor: &#123;
      type: String,
    &#125;,
    isCache: &#123;
      type: Boolean,
      default: false,
    &#125;,
    url: &#123;
      type: String,
      default: url
    &#125;
  &#125;,
  mounted() &#123;
    const colorPicker = localStorage.getItem("colorPicker");
    const &#123; defaultColor &#125; = this;
    // 主题色优先级localStorage.getItem("colorPicker") > defaultColor > ORIGINAL_THEME
    this.theme = this.CheckIsColor(colorPicker)
      ? colorPicker
      : this.CheckIsColor(defaultColor)
      ? defaultColor
      : ORIGINAL_THEME;
  &#125;,
  watch: &#123;
    theme(val) &#123;
      if (typeof val !== "string" || !val) return;
      this.isCache && localStorage.setItem("colorPicker", val);
      const themeCluster = this.getThemeCluster(val.replace("#", ""));
      const originalCluster = this.getThemeCluster(
        ORIGINAL_THEME.replace("#", "")
      );
      const getHandler = (variable, id) => &#123;
        return () => &#123;
          const newStyle = this.updateStyle(
            this[variable],
            originalCluster,
            themeCluster
          );
          let styleTag = document.getElementById(id);
          // 判断是否已经存在标签，么有则生成
          if (!styleTag) &#123;
            styleTag = document.createElement("style");
            styleTag.setAttribute("id", id);
            document.head.appendChild(styleTag);
          &#125;
          // 替换为新的样式表
          styleTag.innerText = newStyle;
        &#125;;
      &#125;;

      const chalkHandler = getHandler("chalk", "chalk-style");
      // 判断是否已有样式表，没有则根据url请求样式表内容
      if (!this.chalk) &#123;
        this.getCSSString(this.url, chalkHandler, "chalk");
      &#125; else &#123;
        chalkHandler();
      &#125;
    &#125;,
  &#125;,

  methods: &#123;
    // 清除缓存
    clearCache() &#123;
      localStorage.removeItem("colorPicker");
    &#125;,
    // 颜色改变
    onChange(e) &#123;
      if (e) &#123;
        this.theme = e;
      &#125;
    &#125;,
    // 判断是否为颜色
    CheckIsColor(bgVal) &#123;
      if (bgVal) &#123;
        var type = "^#[0-9a-fA-F]&#123;6&#125;$";
        var re = new RegExp(type);
        if (bgVal.match(re) == null) &#123;
          type =
            "^[rR][gG][Bb][(]([\\s]*(2[0-4][0-9]|25[0-5]|[01]?[0-9][0-9]?)[\\s]*,)&#123;2&#125;[\\s]*(2[0-4]\\d|25[0-5]|[01]?\\d\\d?)[\\s]*[)]&#123;1&#125;$";
          re = new RegExp(type);
          if (bgVal.match(re) == null) &#123;
            return false;
          &#125; else &#123;
            return true;
          &#125;
        &#125; else &#123;
          return true;
        &#125;
      &#125;
    &#125;,
    // 更新主题系列色
    updateStyle(style, oldCluster, newCluster) &#123;
      let newStyle = style;
      oldCluster.forEach((color, index) => &#123;
        newStyle = newStyle.replace(new RegExp(color, "ig"), newCluster[index]);
      &#125;);
      return newStyle;
    &#125;,
    // 初始化时获取默认主题的样式并复制给this.chalk
    getCSSString(url, callback, variable) &#123;
      const xhr = new XMLHttpRequest();
      xhr.onreadystatechange = () => &#123;
        if (xhr.readyState === 4 && xhr.status === 200) &#123;
          this[variable] = xhr.responseText.replace(/@font-face&#123;[^&#125;]+&#125;/, "");
          callback();
        &#125;
      &#125;;
      xhr.open("GET", url);
      xhr.send();
    &#125;,
    // 获取到系列色
    // 颜色这块别问了，问就是不知道
    getThemeCluster(theme) &#123;
      const tintColor = (color, tint) => &#123;
        let red = parseInt(color.slice(0, 2), 16);
        let green = parseInt(color.slice(2, 4), 16);
        let blue = parseInt(color.slice(4, 6), 16);

        if (tint === 0) &#123;
          return [red, green, blue].join(",");
        &#125; else &#123;
          red += Math.round(tint * (255 - red));
          green += Math.round(tint * (255 - green));
          blue += Math.round(tint * (255 - blue));

          red = red.toString(16);
          green = green.toString(16);
          blue = blue.toString(16);

          return `#$&#123;red&#125;$&#123;green&#125;$&#123;blue&#125;`;
        &#125;
      &#125;;

      const shadeColor = (color, shade) => &#123;
        let red = parseInt(color.slice(0, 2), 16);
        let green = parseInt(color.slice(2, 4), 16);
        let blue = parseInt(color.slice(4, 6), 16);

        red = Math.round((1 - shade) * red);
        green = Math.round((1 - shade) * green);
        blue = Math.round((1 - shade) * blue);

        red = red.toString(16);
        green = green.toString(16);
        blue = blue.toString(16);

        return `#$&#123;red&#125;$&#123;green&#125;$&#123;blue&#125;`;
      &#125;;

      const clusters = [theme];
      for (let i = 0; i <= 9; i++) &#123;
        clusters.push(tintColor(theme, Number((i / 10).toFixed(2))));
      &#125;
      clusters.push(shadeColor(theme, 0.1));
      return clusters;
    &#125;,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">API</h2>
<h3 data-id="heading-5">Attributes</h3>








































<table><thead><tr><th>参数</th><th>说明</th><th>类型</th><th>可选值</th><th>默认值</th></tr></thead><tbody><tr><td>defaultColor</td><td>默认主题</td><td>String</td><td>-</td><td>-</td></tr><tr><td>size</td><td>尺寸大小</td><td>String</td><td>medium、small、mini</td><td>-</td></tr><tr><td>isCache</td><td>是否开启缓存</td><td>Boolean</td><td>-</td><td>false</td></tr><tr><td>url</td><td>加载资源地址</td><td>String</td><td>-</td><td><a href="https://unpkg.com/element-ui@$%7Bversion%7D/lib/theme-chalk/index.css" target="_blank" rel="nofollow noopener noreferrer">unpkg.com/element-ui@…</a></td></tr></tbody></table>
<h3 data-id="heading-6">Methods</h3>















<table><thead><tr><th>方法名</th><th>说明</th><th>参数</th></tr></thead><tbody><tr><td>clearCache</td><td>清楚缓存</td><td>-</td></tr></tbody></table>
<h2 data-id="heading-7">结语</h2>
<p>good good study!!!</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            