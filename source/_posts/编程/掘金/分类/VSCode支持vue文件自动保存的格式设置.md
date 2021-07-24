
---
title: 'VSCode支持.vue文件自动保存的格式设置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8256'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 21:31:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=8256'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0"><strong>实现步骤： 1、安装如下插件</strong></h3>
<p>1)  ESLint： eslint编码规范</p>
<p>2)  Vetur： vue格式化代码</p>
<p>3)  Chinese (Simplified) Language Pack for Visual Studio Code： 中文包</p>
<h3 data-id="heading-1"><strong>2、打开配置文件</strong></h3>
<p>MacOS使用<code>Command + Sheft + P</code>，windows使用<code>Ctrl + Sheft + P</code>快捷键--->
搜索“Configure Language Specific Settings”--->选择“Vue”--->打开配置文件--->将如下代码复制粘贴到配置文件中。</p>
<pre><code class="copyable">&#123;
    // 分号
    "prettier.semi": false,
    "prettier.eslintIntegration": true,
    // 单引号包裹字符串
    // 尽可能控制尾随逗号的打印
    "prettier.trailingComma": "all",
    "prettier.singleQuote": true,
    "prettier.tabWidth": 2,
    // 关闭自带的格式化
    "javascript.format.enable": false,
    // 让函数(名)和后面的括号之间加个空格
    "javascript.format.insertSpaceBeforeFunctionParenthesis": true,
    // 启用eslint
    /*
      该代码为旧版本，已废弃。采用下面的新版本
      "eslint.enable": true, 
      "eslint.validate": [
        "javascript",
        "javascriptreact",
        &#123;
          "language": "vue",
          "autoFix": true
        &#125;
      ],
    */
    "eslint.format.enable": true,
     //autoFix默认开启，只需输入字符串数组即可
     "eslint.validate": ["javascript", "vue", "html"],
    // 格式化.vue中html
    "vetur.format.defaultFormatter.html": "js-beautify-html",
    // 让vue中的js按编辑器自带的ts格式进行格式化
    "vetur.format.defaultFormatter.js": "vscode-typescript",
    "vetur.format.defaultFormatterOptions": &#123;
      "js-beautify-html": &#123;
        // #vue组件中html代码格式化样式
        // "wrap_attributes": "force-expand-multiline"
        // "wrap_attributes": "force"
        // "wrap_attributes": "force-aligned",// 属性强制折行对齐
        "wrap_attributes": "auto"
      &#125;
    &#125;,
    "vetur.format.enable": true,
    "eslint.options": &#123;
      "extensions": [".js", ".vue"]
    &#125;,
    /*
    该版本为旧版本，已经废弃。采用下面的代码
     "eslint.autoFixOnSave": true,
    */ 
    "editor.codeActionsOnSave": &#123;
      "source.fixAll.eslint": true
    &#125;,
    "editor.tabSize": 2,
    // 开启行数提示
    "editor.lineNumbers": "on",
    // 去掉 vscode 自带的自动保存 ，vscode 默认也是 false
    "editor.formatOnSave": false,
    // vscode默认启用了根据文件类型自动设置tabsize的选项
    "editor.detectIndentation": false,
    "editor.quickSuggestions": &#123;
      //开启自动显示建议
      "other": true,
      "comments": true,
      "strings": true
    &#125;,
    "extensions.ignoreRecommendations": false,
    "window.zoomLevel": 1,
    "files.autoGuessEncoding": false,
    "workbench.sideBar.location": "left"
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考连接1：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1720504" target="_blank" rel="nofollow noopener noreferrer" title="https://cloud.tencent.com/developer/article/1720504" ref="nofollow noopener noreferrer">cloud.tencent.com/developer/a…</a></p>
<p>参考连接2：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fvs1435%2Fp%2F11798670.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/vs1435/p/11798670.html" ref="nofollow noopener noreferrer">www.cnblogs.com/vs1435/p/11…</a></p></div>  
</div>
            