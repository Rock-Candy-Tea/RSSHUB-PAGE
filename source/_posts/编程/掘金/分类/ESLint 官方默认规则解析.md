
---
title: 'ESLint 官方默认规则解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5614'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 19:01:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=5614'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>搬运<a href="https://link.juejin.cn/?target=https%3A%2F%2Feslint.bootcss.com%2Fdocs%2Frules%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://eslint.bootcss.com/docs/rules/" ref="nofollow noopener noreferrer">ESLint官方规则说明</a></p>
<h2 data-id="heading-0">值解析</h2>
<ul>
<li><code>"off"</code> or <code>0</code> - 关闭规则</li>
<li><code>"warn"</code> or <code>1</code> - 将规则视为一个警告（不会导致程序退出）</li>
<li><code>"error"</code> or <code>2</code> - 将规则视为一个错误 (当被触发的时候，程序会退出)</li>
</ul>
<h2 data-id="heading-1">规则解析</h2>
<p><code>[es]</code> 表示<code>eslint:recommended</code>推荐启用的规则, 注释是说明此规则的解释，值只表示关闭、警告或者报告错误此规则。</p>
<h3 data-id="heading-2">Possible Errors</h3>
<p>这些规则与 JavaScript 代码中可能的错误或逻辑错误有关</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"for-direction"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制 “for” 循环中更新子句的计数器朝着正确的方向移动 [es]</span>
<span class="hljs-string">"getter-return"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制 getter 函数中出现 return 语句 [es]</span>
<span class="hljs-string">"no-async-promise-executor"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止使用异步函数作为 Promise executor [es]</span>
<span class="hljs-string">"no-await-in-loop"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在循环中出现 await</span>
<span class="hljs-string">"no-compare-neg-zero"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止与 -0 进行比较 [es]</span>
<span class="hljs-string">"no-cond-assign"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止条件表达式中出现赋值操作符 [es]</span>
<span class="hljs-string">"no-console"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 console</span>
<span class="hljs-string">"no-constant-condition"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止在条件中使用常量表达式 if(true) if(1) [es]</span>
<span class="hljs-string">"no-control-regex"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止在正则表达式中使用控制字符 [es]</span>
<span class="hljs-string">"no-debugger"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用 debugger [es]</span>
<span class="hljs-string">"no-dupe-args"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止 function 定义中出现重名参数 [es]</span>
<span class="hljs-string">"no-dupe-keys"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止对象字面量中出现重复的 key [es]</span>
<span class="hljs-string">"no-duplicate-case"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止出现重复的 case 标签 [es]</span>
<span class="hljs-string">"no-empty"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止出现空语句块 [es]</span>
<span class="hljs-string">"no-empty-character-class"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止在正则表达式中使用空字符集([]内容不能为空) [es]</span>
<span class="hljs-string">"no-ex-assign"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止对 catch 子句的参数重新赋值 [es]</span>
<span class="hljs-string">"no-extra-boolean-cast"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止不必要的布尔转换 [es]</span>
<span class="hljs-string">"no-extra-parens"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止不必要的括号</span>
<span class="hljs-string">"no-extra-semi"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止不必要的分号 [es]</span>
<span class="hljs-string">"no-func-assign"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止对 function 声明重新赋值 [es]</span>
<span class="hljs-string">"no-inner-declarations"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止在嵌套的块中出现变量声明或 function 声明 [es]</span>
<span class="hljs-string">"no-invalid-regexp"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止 RegExp 构造函数中存在无效的正则表达式字符串 [es]</span>
<span class="hljs-string">"no-irregular-whitespace"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止不规则的空白 [es]</span>
<span class="hljs-string">"no-misleading-character-class"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 不允许在字符类语法中出现由多个代码点组成的字符 [es]</span>
<span class="hljs-string">"no-obj-calls"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止把全局对象作为函数调用,比如Math() JSON() [es]</span>
<span class="hljs-string">"no-prototype-builtins"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止直接调用 Object.prototypes 的内置属性 [es]</span>
<span class="hljs-string">"no-regex-spaces"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止正则表达式字面量中出现多个空格 [es]</span>
<span class="hljs-string">"no-sparse-arrays"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用稀疏数组,比如[1,,2] [es]</span>
<span class="hljs-string">"no-template-curly-in-string"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在常规字符串中出现模板字面量占位符语法</span>
<span class="hljs-string">"no-unexpected-multiline"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止出现令人困惑的多行表达式 [es]</span>
<span class="hljs-string">"no-unreachable"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止在 return、throw、continue 和 break 语句之后出现不可达代码 [es]</span>
<span class="hljs-string">"no-unsafe-finally"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止在 finally 语句块中出现控制流语句 [es]</span>
<span class="hljs-string">"no-unsafe-negation"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止对关系运算符的左操作数使用否定操作符 [es]</span>
<span class="hljs-string">"require-atomic-updates"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止由于 await 或 yield的使用而可能导致出现竞态条件的赋值 [es]</span>
<span class="hljs-string">"use-isnan"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 要求使用 isNaN() 检查 NaN [es]</span>
<span class="hljs-string">"valid-typeof"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制 typeof 表达式与有效的字符串进行比较 [es]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">Best Practices</h3>
<p>这些规则是关于最佳实践的，帮助你避免出现一些问题</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"accessor-pairs"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制 getter 和 setter 在对象中成对出现</span>
<span class="hljs-string">"array-callback-return"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制数组方法的回调函数中有 return 语句</span>
<span class="hljs-string">"block-scoped-var"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制把变量的使用限制在其定义的作用域范围内</span>
<span class="hljs-string">"class-methods-use-this"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制类方法使用 this</span>
<span class="hljs-string">"complexity"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 指定程序中允许的最大环路复杂度</span>
<span class="hljs-string">"consistent-return"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求 return 语句要么总是指定返回的值，要么不指定</span>
<span class="hljs-string">"curly"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制所有控制语句使用一致的括号风格</span>
<span class="hljs-string">"default-case"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求 switch 语句中有 default 分支</span>
<span class="hljs-string">"dot-location"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在点号之前和之后一致的换行</span>
<span class="hljs-string">"dot-notation"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制尽可能地使用点号</span>
<span class="hljs-string">"eqeqeq"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求使用 === 和 !==</span>
<span class="hljs-string">"guard-for-in"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求 for-in 循环中有一个 if 语句</span>
<span class="hljs-string">"max-classes-per-file"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制每个文件中包含的的类的最大数量,默认1, [0,1]</span>
<span class="hljs-string">"no-alert"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 alert、confirm 和 prompt</span>
<span class="hljs-string">"no-caller"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 arguments.caller 或 arguments.callee</span>
<span class="hljs-string">"no-case-declarations"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 不允许在 case 子句中使用词法声明 [es]</span>
<span class="hljs-string">"no-div-regex"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止除法操作符显式的出现在正则表达式开始的位置</span>
<span class="hljs-string">"no-else-return"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止 if 语句中 return 语句之后有 else 块</span>
<span class="hljs-string">"no-empty-function"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止出现空函数</span>
<span class="hljs-string">"no-empty-pattern"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止使用空解构模式 [es]</span>
<span class="hljs-string">"no-eq-null"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在没有类型检查操作符的情况下与 null 进行比较</span>
<span class="hljs-string">"no-eval"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 eval()</span>
<span class="hljs-string">"no-extend-native"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止扩展原生类型</span>
<span class="hljs-string">"no-extra-bind"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止不必要的 .bind() 调用</span>
<span class="hljs-string">"no-extra-label"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用不必要的标签</span>
<span class="hljs-string">"no-fallthrough"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止 case 语句落空 [es]</span>
<span class="hljs-string">"no-floating-decimal"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止数字字面量中使用前导和末尾小数点</span>
<span class="hljs-string">"no-global-assign"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止对原生对象或只读的全局对象进行赋值 [es]</span>
<span class="hljs-string">"no-implicit-coercion"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止使用短符号进行类型转换</span>
<span class="hljs-string">"no-implicit-globals"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在全局范围内使用变量声明和 function 声明</span>
<span class="hljs-string">"no-implied-eval"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止使用类似 eval() 的方法</span>
<span class="hljs-string">"no-invalid-this"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止 this 关键字出现在类和类对象之外</span>
<span class="hljs-string">"no-iterator"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 __iterator__ 属性</span>
<span class="hljs-string">"no-labels"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用标签语句</span>
<span class="hljs-string">"no-lone-blocks"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用不必要的嵌套块</span>
<span class="hljs-string">"no-loop-func"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在循环语句中出现包含不安全引用的函数声明(如果没有引用外部变量不形成闭包就可以)</span>
<span class="hljs-string">"no-magic-numbers"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用魔术数字</span>
<span class="hljs-string">"no-multi-spaces"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止使用多个空格</span>
<span class="hljs-string">"no-multi-str"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止使用多行字符串</span>
<span class="hljs-string">"no-new"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止使用 new 以避免产生副作用</span>
<span class="hljs-string">"no-new-func"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止对 Function 对象使用 new 操作符</span>
<span class="hljs-string">"no-new-wrappers"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止对 String，Number 和 Boolean 使用 new 操作符</span>
<span class="hljs-string">"no-octal"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用八进制字面量 [es]</span>
<span class="hljs-string">"no-octal-escape"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在字符串中使用八进制转义序列</span>
<span class="hljs-string">"no-param-reassign"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止对 function 的参数进行重新赋值</span>
<span class="hljs-string">"no-proto"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 __proto__ 属性</span>
<span class="hljs-string">"no-redeclare"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止多次声明同一变量 [es]</span>
<span class="hljs-string">"no-restricted-properties"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止使用对象的某些属性</span>
<span class="hljs-string">"no-return-assign"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在 return 语句中使用赋值语句</span>
<span class="hljs-string">"no-return-await"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用不必要的 return await</span>
<span class="hljs-string">"no-script-url"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止使用 javascript: url</span>
<span class="hljs-string">"no-self-assign"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止自我赋值 [es]</span>
<span class="hljs-string">"no-self-compare"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止自身比较</span>
<span class="hljs-string">"no-sequences"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用逗号操作符</span>
<span class="hljs-string">"no-throw-literal"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止抛出异常字面量</span>
<span class="hljs-string">"no-unmodified-loop-condition"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用一成不变的循环条件</span>
<span class="hljs-string">"no-unused-expressions"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止出现未使用过的表达式</span>
<span class="hljs-string">"no-unused-labels"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用出现未使用过的标签 [es]</span>
<span class="hljs-string">"no-useless-call"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止不必要的 .call() 和 .apply()</span>
<span class="hljs-string">"no-useless-catch"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止不必要的 catch 子句 [es]</span>
<span class="hljs-string">"no-useless-concat"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止不必要的字符串字面量或模板字面量的连接</span>
<span class="hljs-string">"no-useless-escape"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用不必要的转义字符 [es]</span>
<span class="hljs-string">"no-useless-return"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止多余的 return 语句</span>
<span class="hljs-string">"no-void"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 void 操作符</span>
<span class="hljs-string">"no-warning-comments"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在注释中使用特定的警告术语</span>
<span class="hljs-string">"no-with"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用 with 语句 [es]</span>
<span class="hljs-string">"prefer-named-capture-group"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 建议在正则表达式中使用命名捕获组</span>
<span class="hljs-string">"prefer-promise-reject-errors"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求使用 Error 对象作为 Promise 拒绝的原因</span>
<span class="hljs-string">"radix"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在 parseInt() 使用基数参数</span>
<span class="hljs-string">"require-await"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止使用不带 await 表达式的 async 函数</span>
<span class="hljs-string">"require-unicode-regexp"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在 RegExp 上使用 u 标志</span>
<span class="hljs-string">"vars-on-top"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求所有的 var 声明出现在它们所在的作用域顶部</span>
<span class="hljs-string">"wrap-iife"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求 IIFE 使用括号括起来</span>
<span class="hljs-string">"yoda"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止 “Yoda” 条件</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">Strict Mode</h3>
<p>该规则与使用严格模式和严格模式指令有关</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"strict"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止使用严格模式指令</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Variables</h3>
<p>这些规则与变量声明有关</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"init-declarations"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止 var 声明中的初始化</span>
<span class="hljs-string">"no-delete-var"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止删除变量 [es]</span>
<span class="hljs-string">"no-label-var"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 不允许标签与变量同名</span>
<span class="hljs-string">"no-restricted-globals"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用特定的全局变量</span>
<span class="hljs-string">"no-shadow"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止变量声明与外层作用域的变量同名</span>
<span class="hljs-string">"no-shadow-restricted-names"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止将标识符定义为受限的名字 [es]</span>
<span class="hljs-string">"no-undef"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用未声明的变量，除非它们在 /*global */ 注释中被提到 [es]</span>
<span class="hljs-string">"no-undef-init"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止将变量初始化为 undefined</span>
<span class="hljs-string">"no-undefined"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止将 undefined 作为标识符</span>
<span class="hljs-string">"no-unused-vars"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止出现未使用过的变量 [es]</span>
<span class="hljs-string">"no-use-before-define"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在变量定义之前使用它们</span>
<span class="hljs-string">""</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">Node.js and CommonJS</h3>
<p>这些规则是关于Node.js 或 在浏览器中使用CommonJS 的</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"callback-return"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制数组方法的回调函数中有 return 语句</span>
<span class="hljs-string">"global-require"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求 require() 出现在顶层模块作用域中</span>
<span class="hljs-string">"handle-callback-err"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求回调函数中有容错处理 </span>
<span class="hljs-string">"no-buffer-constructor"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 Buffer() 构造函数</span>
<span class="hljs-string">"no-mixed-requires"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止混合常规变量声明和 require 调用</span>
<span class="hljs-string">"no-new-require"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止调用 require 时使用 new 操作符</span>
<span class="hljs-string">"no-path-concat"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止对 __dirname 和 __filename 进行字符串连接</span>
<span class="hljs-string">"no-process-env"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 process.env</span>
<span class="hljs-string">"no-process-exit"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 process.exit()</span>
<span class="hljs-string">"no-restricted-modules"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用通过 require 加载的指定模块</span>
<span class="hljs-string">"no-sync"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用同步方法</span>
<span class="hljs-string">""</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">ECMAScript 6</h3>
<p>这些规则只与 ES6 有关, 即通常所说的 ES2015</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"arrow-body-style"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求箭头函数体使用大括号</span>
<span class="hljs-string">"arrow-parens"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求箭头函数的参数使用圆括号</span>
<span class="hljs-string">"arrow-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制箭头函数的箭头前后使用一致的空格</span>
<span class="hljs-string">"constructor-super"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 要求在构造函数中有 super() 的调用 [es]</span>
<span class="hljs-string">"generator-star-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制 generator 函数中 * 号周围使用一致的空格</span>
<span class="hljs-string">"no-class-assign"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止修改类声明的变量 [es]</span>
<span class="hljs-string">"no-confusing-arrow"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在可能与比较操作符相混淆的地方使用箭头函数</span>
<span class="hljs-string">"no-const-assign"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止修改 const 声明的变量 [es]</span>
<span class="hljs-string">"no-dupe-class-members"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止类成员中出现重复的名称 [es]</span>
<span class="hljs-string">"no-duplicate-imports"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止重复模块导入</span>
<span class="hljs-string">"no-new-symbol"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止 Symbolnew 操作符和 new 一起使用 [es]</span>
<span class="hljs-string">"no-restricted-imports"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止使用指定的 import 加载的模块</span>
<span class="hljs-string">"no-this-before-super"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止在构造函数中，在调用 super() 之前使用 this 或 super [es]</span>
<span class="hljs-string">"no-useless-computed-key"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在对象中使用不必要的计算属性</span>
<span class="hljs-string">"no-useless-constructor"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用不必要的构造函数</span>
<span class="hljs-string">"no-useless-rename"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在 import 和 export 和解构赋值时将引用重命名为相同的名字</span>
<span class="hljs-string">"no-var"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求使用 let 或 const 而不是 var</span>
<span class="hljs-string">"object-shorthand"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止对象字面量中方法和属性使用简写语法</span>
<span class="hljs-string">"prefer-arrow-callback"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求回调函数使用箭头函数</span>
<span class="hljs-string">"prefer-const"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求使用 const 声明那些声明后不再被修改的变量</span>
<span class="hljs-string">"prefer-destructuring"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 优先使用数组和对象解构</span>
<span class="hljs-string">"prefer-numeric-literals"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 parseInt() 和 Number.parseInt()，使用二进制，八进制和十六进制字面量</span>
<span class="hljs-string">"prefer-rest-params"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求使用剩余参数而不是 arguments</span>
<span class="hljs-string">"prefer-spread"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求使用扩展运算符而非 .apply()</span>
<span class="hljs-string">"prefer-template"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求使用模板字面量而非字符串连接</span>
<span class="hljs-string">"require-yield"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 要求 generator 函数内有 yield [es]</span>
<span class="hljs-string">"rest-spread-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制剩余和扩展运算符及其表达式之间有空格</span>
<span class="hljs-string">"sort-imports"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制模块内的 import 排序</span>
<span class="hljs-string">"symbol-description"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求 symbol 描述</span>
<span class="hljs-string">"template-curly-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止模板字符串中的嵌入表达式周围空格的使用</span>
<span class="hljs-string">"yield-star-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在 yield* 表达式中 * 周围使用空格 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Stylistic Issues</h3>
<p>这些规则是关于风格指南的，而且是非常主观的</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"array-bracket-newline"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 在数组开括号后和闭括号前强制换行</span>
<span class="hljs-string">"array-bracket-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制数组方括号中使用一致的空格</span>
<span class="hljs-string">"array-element-newline"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制数组元素间出现换行</span>
<span class="hljs-string">"block-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止或强制在代码块中开括号前和闭括号后有空格</span>
<span class="hljs-string">"brace-style"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在代码块中使用一致的大括号风格</span>
<span class="hljs-string">"camelcase"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制使用骆驼拼写法命名约定</span>
<span class="hljs-string">"capitalized-comments"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制或禁止对注释的第一个字母大写</span>
<span class="hljs-string">"comma-dangle"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止末尾逗号</span>
<span class="hljs-string">"comma-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在逗号前后使用一致的空格</span>
<span class="hljs-string">"comma-style"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制使用一致的逗号风格</span>
<span class="hljs-string">"computed-property-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在计算的属性的方括号中使用一致的空格</span>
<span class="hljs-string">"consistent-this"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 当获取当前执行环境的上下文时，强制使用一致的命名</span>
<span class="hljs-string">"eol-last"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止文件末尾存在空行</span>
<span class="hljs-string">"func-call-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止在函数标识符和其调用之间有空格</span>
<span class="hljs-string">"func-name-matching"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求函数名与赋值给它们的变量名或属性名相匹配</span>
<span class="hljs-string">"func-names"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止使用命名的 function 表达式</span>
<span class="hljs-string">"func-style"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制一致地使用 function 声明或表达式</span>
<span class="hljs-string">"function-paren-newline"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在函数括号内使用一致的换行</span>
<span class="hljs-string">"id-blacklist"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用指定的标识符</span>
<span class="hljs-string">"id-length"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制标识符的最小和最大长度</span>
<span class="hljs-string">"id-match"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求标识符匹配一个指定的正则表达式</span>
<span class="hljs-string">"implicit-arrow-linebreak"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制隐式返回的箭头函数体的位置</span>
<span class="hljs-string">"indent"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制使用一致的缩进</span>
<span class="hljs-string">"jsx-quotes"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在 JSX 属性中一致地使用双引号或单引号</span>
<span class="hljs-string">"key-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在对象字面量的属性中键和值之间使用一致的间距</span>
<span class="hljs-string">"keyword-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在关键字前后使用一致的空格</span>
<span class="hljs-string">"line-comment-position"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制行注释的位置</span>
<span class="hljs-string">"linebreak-style"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制使用一致的换行风格</span>
<span class="hljs-string">"lines-around-comment"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求在注释周围有空行</span>
<span class="hljs-string">"lines-between-class-members"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止类成员之间出现空行</span>
<span class="hljs-string">"max-depth"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制可嵌套的块的最大深度</span>
<span class="hljs-string">"max-len"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制一行的最大长度</span>
<span class="hljs-string">"max-lines"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制最大行数</span>
<span class="hljs-string">"max-lines-per-function"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制函数最大代码行数</span>
<span class="hljs-string">"max-nested-callbacks"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制回调函数最大嵌套深度</span>
<span class="hljs-string">"max-params"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制函数定义中最多允许的参数数量</span>
<span class="hljs-string">"max-statements"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制函数块最多允许的的语句数量</span>
<span class="hljs-string">"max-statements-per-line"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制每一行中所允许的最大语句数量</span>
<span class="hljs-string">"multiline-comment-style"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制对多行注释使用特定风格</span>
<span class="hljs-string">"multiline-ternary"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止在三元操作数中间换行</span>
<span class="hljs-string">"new-cap"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求构造函数首字母大写</span>
<span class="hljs-string">"new-parens"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制或禁止调用无参构造函数时有圆括号</span>
<span class="hljs-string">"newline-per-chained-call"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求方法链中每个调用都有一个换行符</span>
<span class="hljs-string">"no-array-constructor"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 Array 构造函数</span>
<span class="hljs-string">"no-bitwise"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用按位运算符</span>
<span class="hljs-string">"no-continue"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 continue 语句</span>
<span class="hljs-string">"no-inline-comments"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在代码后使用内联注释</span>
<span class="hljs-string">"no-lonely-if"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止 if 作为唯一的语句出现在 else 语句中</span>
<span class="hljs-string">"no-mixed-operators"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止混合使用不同的操作符</span>
<span class="hljs-string">"no-mixed-spaces-and-tabs"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止空格和 tab 的混合缩进 [es]</span>
<span class="hljs-string">"no-multi-assign"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止连续赋值</span>
<span class="hljs-string">"no-multiple-empty-lines"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止出现多行空行</span>
<span class="hljs-string">"no-negated-condition"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用否定的表达式</span>
<span class="hljs-string">"no-nested-ternary"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用嵌套的三元表达式</span>
<span class="hljs-string">"no-new-object"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 Object 的构造函数</span>
<span class="hljs-string">"no-plusplus"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用一元操作符 ++ 和 --</span>
<span class="hljs-string">"no-restricted-syntax"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用特定的语法</span>
<span class="hljs-string">"no-tabs"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 tab</span>
<span class="hljs-string">"no-ternary"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用三元操作符</span>
<span class="hljs-string">"no-trailing-spaces"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用行尾空格</span>
<span class="hljs-string">"no-underscore-dangle"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止标识符中有悬空下划线</span>
<span class="hljs-string">"no-unneeded-ternary"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止可以在有更简单的可替代的表达式时使用三元操作符</span>
<span class="hljs-string">"no-whitespace-before-property"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止属性前有空白</span>
<span class="hljs-string">"nonblock-statement-body-position"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制单个语句的位置</span>
<span class="hljs-string">"object-curly-newline"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制大括号内换行符的一致性</span>
<span class="hljs-string">"object-curly-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在大括号中使用一致的空格</span>
<span class="hljs-string">"object-property-newline"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制将对象的属性放在不同的行上</span>
<span class="hljs-string">"one-var"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制函数中的变量要么一起声明要么分开声明</span>
<span class="hljs-string">"one-var-declaration-per-line"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止在变量声明周围换行</span>
<span class="hljs-string">"operator-assignment"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止在可能的情况下使用简化的赋值操作符</span>
<span class="hljs-string">"operator-linebreak"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制操作符使用一致的换行符</span>
<span class="hljs-string">"padded-blocks"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止块内填充</span>
<span class="hljs-string">"padding-line-between-statements"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止在语句间填充空行</span>
<span class="hljs-string">"prefer-object-spread"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止使用以对象字面量作为第一个参数的 Object.assign，优先使用对象扩展。</span>
<span class="hljs-string">"quote-props"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求对象字面量属性名称用引号括起来</span>
<span class="hljs-string">"quotes"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制使用一致的反勾号、双引号或单引号</span>
<span class="hljs-string">"semi"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止使用分号代替 ASI</span>
<span class="hljs-string">"semi-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制分号之前和之后使用一致的空格</span>
<span class="hljs-string">"semi-style"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制分号的位置</span>
<span class="hljs-string">"sort-keys"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求对象属性按序排列</span>
<span class="hljs-string">"sort-vars"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求同一个声明块中的变量按顺序排列</span>
<span class="hljs-string">"space-before-blocks"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在块之前使用一致的空格</span>
<span class="hljs-string">"space-before-function-paren"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在 function的左括号之前使用一致的空格</span>
<span class="hljs-string">"space-in-parens"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在圆括号内使用一致的空格</span>
<span class="hljs-string">"space-infix-ops"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求操作符周围有空格</span>
<span class="hljs-string">"space-unary-ops"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在一元操作符前后使用一致的空格</span>
<span class="hljs-string">"spaced-comment"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在注释中 // 或 /* 使用一致的空格</span>
<span class="hljs-string">"switch-colon-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 强制在 switch 的冒号左右有空格</span>
<span class="hljs-string">"template-tag-spacing"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止在模板标记和它们的字面量之间有空格</span>
<span class="hljs-string">"unicode-bom"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求或禁止 Unicode 字节顺序标记 (BOM)</span>
<span class="hljs-string">"wrap-regex"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求正则表达式被括号括起来</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">我在使用的 Rules</h2>
<pre><code class="hljs language-json copyable" lang="json">    <span class="hljs-string">"arrow-spacing"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制箭头函数的箭头前后使用一致的空格</span>
    <span class="hljs-string">"block-spacing"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"always"</span>], <span class="hljs-comment">// 禁止或强制在代码块中开括号前和闭括号后有空格</span>
    <span class="hljs-string">"brace-style"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"1tbs"</span>, &#123;
      <span class="hljs-attr">"allowSingleLine"</span>: <span class="hljs-literal">true</span>
    &#125;], <span class="hljs-comment">// 强制在代码块中使用一致的大括号风格</span>
    <span class="hljs-string">"comma-dangle"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 要求或禁止末尾逗号</span>
    <span class="hljs-string">"comma-spacing"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制在逗号前后使用一致的空格</span>
    <span class="hljs-string">"comma-style"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制使用一致的逗号风格</span>
    <span class="hljs-string">"curly"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"multi-line"</span>], <span class="hljs-comment">// 强制所有控制语句使用一致的括号风格</span>
    <span class="hljs-string">"eol-last"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 要求或禁止文件末尾存在空行</span>
    <span class="hljs-string">"eqeqeq"</span>: [<span class="hljs-string">"error"</span>, <span class="hljs-string">"smart"</span>], <span class="hljs-comment">// 要求使用 === 和 !==</span>
    <span class="hljs-string">"guard-for-in"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 要求 for-in 循环中有一个 if 语句</span>
    <span class="hljs-string">"handle-callback-err"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"^(err|error)$"</span>], <span class="hljs-comment">// 要求回调函数中有容错处理 </span>
    <span class="hljs-string">"indent"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"tab"</span>, &#123;
      <span class="hljs-attr">"SwitchCase"</span>: <span class="hljs-number">1</span>
    &#125;], <span class="hljs-comment">// 强制使用一致的缩进</span>
    <span class="hljs-string">"jsx-quotes"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"prefer-single"</span>], <span class="hljs-comment">// 强制在 JSX 属性中一致地使用双引号或单引号</span>
    <span class="hljs-string">"key-spacing"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制在对象字面量的属性中键和值之间使用一致的间距</span>
    <span class="hljs-string">"keyword-spacing"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制在关键字前后使用一致的空格</span>
    <span class="hljs-string">"new-cap"</span>: [<span class="hljs-number">2</span>, &#123;
      <span class="hljs-attr">"capIsNew"</span>: <span class="hljs-literal">false</span>
    &#125;], <span class="hljs-comment">// 要求构造函数首字母大写</span>
    <span class="hljs-string">"new-parens"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制或禁止调用无参构造函数时有圆括号</span>
    <span class="hljs-string">"no-array-constructor"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用 Array 构造函数</span>
    <span class="hljs-string">"no-control-regex"</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁止在正则表达式中使用控制字符</span>
    <span class="hljs-string">"no-label-var"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 不允许标签与变量同名</span>
    <span class="hljs-string">"no-multiple-empty-lines"</span>: [<span class="hljs-number">2</span>, &#123;
      <span class="hljs-attr">"max"</span>: <span class="hljs-number">1</span>
    &#125;], <span class="hljs-comment">// 禁止出现多行空行</span>
    <span class="hljs-string">"no-new-object"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用 Object 的构造函数</span>
    <span class="hljs-string">"no-new-require"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止调用 require 时使用 new 操作符</span>
    <span class="hljs-string">"no-path-concat"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">//  禁止对 __dirname 和 __filename 进行字符串连接</span>
    <span class="hljs-string">"no-throw-literal"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止抛出异常字面量</span>
    <span class="hljs-string">"no-trailing-spaces"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用行尾空格</span>
    <span class="hljs-string">"no-undef-init"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止将变量初始化为 undefined</span>
    <span class="hljs-string">"no-unmodified-loop-condition"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用一成不变的循环条件</span>
    <span class="hljs-string">"no-unneeded-ternary"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止可以在有更简单的可替代的表达式时使用三元操作符</span>
    <span class="hljs-string">"no-useless-call"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止不必要的 .call() 和 .apply()</span>
    <span class="hljs-string">"no-useless-computed-key"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止在对象中使用不必要的计算属性</span>
    <span class="hljs-string">"no-useless-constructor"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁用不必要的构造函数</span>
    <span class="hljs-string">"no-whitespace-before-property"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 禁止属性前有空白</span>
    <span class="hljs-string">"one-var"</span>: [<span class="hljs-number">2</span>, &#123;
      <span class="hljs-attr">"initialized"</span>: <span class="hljs-string">"never"</span>
    &#125;], <span class="hljs-comment">// 强制函数中的变量要么一起声明要么分开声明</span>
    <span class="hljs-string">"operator-linebreak"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制操作符使用一致的换行符</span>
    <span class="hljs-string">"padded-blocks"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"always"</span>, &#123;
      <span class="hljs-attr">"blocks"</span>: <span class="hljs-string">"never"</span>,
      <span class="hljs-attr">"classes"</span>: <span class="hljs-string">"always"</span>,
      <span class="hljs-attr">"switches"</span>: <span class="hljs-string">"never"</span> 
    &#125;], <span class="hljs-comment">// 要求或禁止块内填充</span>
    <span class="hljs-string">"quotes"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"single"</span>], <span class="hljs-comment">// 强制使用一致的反勾号、双引号或单引号</span>
    <span class="hljs-string">"semi"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"never"</span>,&#123;
      <span class="hljs-attr">"beforeStatementContinuationChars"</span>: <span class="hljs-string">"always"</span> <span class="hljs-comment">// 如果下一句以 [、(、/、+ 或 - 开头，要求句末有分号</span>
    &#125;], <span class="hljs-comment">// 要求或禁止使用分号代替 ASI</span>
    <span class="hljs-string">"semi-spacing"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制分号前后有空格</span>
    <span class="hljs-string">"space-before-blocks"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制在块之前使用一致的空格</span>
    <span class="hljs-string">"space-before-function-paren"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制在 function的左括号之前使用一致的空格</span>
    <span class="hljs-string">"space-in-parens"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制在圆括号内使用一致的空格</span>
    <span class="hljs-string">"space-infix-ops"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 要求操作符周围有空格</span>
    <span class="hljs-string">"space-unary-ops"</span>: [<span class="hljs-number">2</span>, &#123;
      <span class="hljs-attr">"words"</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">"nonwords"</span>: <span class="hljs-literal">false</span>
    &#125;], <span class="hljs-comment">// 强制在一元操作符前后使用一致的空格</span>
    <span class="hljs-string">"spaced-comment"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"always"</span>, &#123;
      <span class="hljs-attr">"markers"</span>: [<span class="hljs-string">"global"</span>, <span class="hljs-string">"globals"</span>, <span class="hljs-string">"eslint"</span>, <span class="hljs-string">"eslint-disable"</span>, <span class="hljs-string">"*package"</span>, <span class="hljs-string">"!"</span>, <span class="hljs-string">","</span>]
    &#125;], <span class="hljs-comment">// 强制在注释中 // 或 /* 使用一致的空格</span>
    <span class="hljs-string">"template-curly-spacing"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 要求或禁止模板字符串中的嵌入表达式周围空格的使用</span>
    <span class="hljs-string">"wrap-iife"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"any"</span>], <span class="hljs-comment">// 要求 IIFE 使用括号括起来</span>
    <span class="hljs-string">"yield-star-spacing"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"both"</span>], <span class="hljs-comment">// 强制在 yield* 表达式中 * 周围使用空格</span>
    <span class="hljs-string">"yoda"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"never"</span>], <span class="hljs-comment">// 要求或禁止 “Yoda” 条件</span>
    <span class="hljs-string">"prefer-const"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 要求使用 const 声明那些声明后不再被修改的变量</span>
    <span class="hljs-string">"no-debugger"</span>: process.env.NODE_ENV === <span class="hljs-string">"production"</span> ? <span class="hljs-number">2</span> : <span class="hljs-number">0</span>, <span class="hljs-comment">// 禁用 debugger</span>
    <span class="hljs-string">"object-curly-spacing"</span>: [<span class="hljs-number">2</span>, <span class="hljs-string">"always"</span>, &#123; 
      <span class="hljs-attr">"arraysInObjects"</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">"objectsInObjects"</span>: <span class="hljs-literal">false</span>
    &#125;], <span class="hljs-comment">// 强制在大括号中使用一致的空格</span>
    <span class="hljs-string">"array-bracket-spacing"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 强制数组方括号中使用一致的空格</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            