
---
title: '脚手架系列-commander'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cc3e45f5ab64e29bafd2c2b31f9e1d2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 07 May 2021 19:08:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cc3e45f5ab64e29bafd2c2b31f9e1d2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">开始</h1>
<p>最近看了vue/cli的源代码，学习到了许多相关的核心工具库，打算输出一系列的核心知识文章。</p>
<p>本篇为脚手架系列第一篇，后面不定期更新（手动狗头），先挖一个坑。</p>
<p>在阅读源码或者自己实现一个脚手架工具前，先要熟悉并学会使用一些工具。本篇文章先从命令行工具commander开始学习！</p>
<h1 data-id="heading-1">commander</h1>
<p><code>commander</code>是一款重量轻，表现力和强大的命令行框架，提供了用户命令行输入和参数解析强大功能。</p>
<p>这个工具就是在你输入对应的命令时返回对应的消息，比如vue-cli，你在系统全局安装了cli工具后，在命令提示框输入对应的命令后会弹出相应的交互信息，如下截图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cc3e45f5ab64e29bafd2c2b31f9e1d2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">使用方式</h3>
<p><strong>本次教程使用的版本为：6.2.0</strong></p>
<p><strong>官方地址：<a href="https://github.com/tj/commander.js" target="_blank" rel="nofollow noopener noreferrer">github.com/tj/commande…</a></strong></p>
<p>先安装</p>
<pre><code class="copyable">npm i commander
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入全局对象</p>
<pre><code class="copyable">const &#123; program &#125; = require('commander');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>官方教程还有一个引入Command来实例化program对象的方式</p>
<pre><code class="copyable">const &#123; Command &#125; = require('commander');
const program = new Command();
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>注意：在执行相关的命令后，要在控制台打印相关的信息的话，必须在最后执行以下这句代码。</strong></p>
</blockquote>
<pre><code class="copyable">program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">version()方法</h3>
<p>这个方法可以用来输出当前你的脚手架工具的版本号。</p>
<h4 data-id="heading-4">参数</h4>
<ul>
<li>版本号，必须参数</li>
<li>自定义命令标识，可选参数，默认为<code>-V</code>或<code>--version</code></li>
<li>描述信息，可选参数</li>
</ul>
<pre><code class="copyable">// 只有版本信息
program.version('1.0.0');

program.prase(process.argv);

// 自定义命令标识
// 添加了自定义参数后，执行命令就可以使用自己定义的参数了
program.version('1.0.0', '-v, --vers');

program.prase(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">options()方法</h3>
<p><code>Commander</code>使用<code>option()</code>方法来定义选项，同时可以附加选项的简介。每个选项可以定义一个短选项名称（-后面接单个字符）和一个长选项名称（--后面接一个或多个单词），使用逗号、空格或|分隔。</p>
<h4 data-id="heading-6">参数</h4>
<ul>
<li>自定义命令标识，必须参数
<ul>
<li>一长一断的标识，使用逗号、空格或|分隔</li>
<li>标识后面可以跟参数，<code><></code>为必须参数，<code>[]</code>为可选参数，如<code>-t --test <type></code></li>
</ul>
</li>
<li>选项描述，可选参数，这个在你使用<code>-h</code>或<code>--help</code>参数时会显示对应的信息</li>
<li>选项的默认值，可选参数</li>
</ul>
<h4 data-id="heading-7">基本用法</h4>
<blockquote>
<p>选项可以通过<code>Commander</code>对象的同名属性获取，对于多个单词的长选项，使用驼峰法获取，例如<code>--template-engine</code>与属性<code>program.templateEngine</code>关联。比如下面演示代码的<code>--debug-test</code>参数</p>
</blockquote>
<pre><code class="copyable">program.version('1.1.0')
  .option('-t, --test', 'test option function')
  .option('-d, --debug-test', 'test option function -- debug test');

// 注意，在执行相关的命令后，要在控制台打印相关的信息的话，必须在最后执行以下这句代码。
program.parse(process.argv);

console.log('----------------');
if(program.test) &#123;
  console.log('you use --test commander');
&#125;
if(program.debugTest) &#123;
  console.log('you use --debug-test commander');
&#125;
console.log('----------------');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当你在执行这段代码对应的文件时，比如<code>node xxx.js -t</code>或<code>node xxx.js --test</code>，会输出<code>you use --test commander</code>。<code>node xxx.js -d</code>或<code>node xxx.js --debug-test</code>，会输出<code>you use --debug-test commander</code>。</p>
<h4 data-id="heading-8">带参数和加默认值</h4>
<p>可以在命令后面带参数，使用<>来声明</p>
<pre><code class="copyable">program.version('1.1.0')
  .option('-a, --argu-test <name>', 'test option function -- agru test') // 带参数<>

// 注意，在执行相关的命令后，要在控制台打印相关的信息的话，必须在最后执行以下这句代码。
program.parse(process.argv);

console.log('----------------');
if(program.arguTest) &#123;
  console.log(`output: $&#123;program.arguTest&#125;`);
&#125;
console.log('----------------');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行<code>node xxx.js --argu-test=hello</code>或<code>node xxx.js -a hello</code>，则会输出<code>output: hello</code></p>
<blockquote>
<p>注意：如果我们定义了<>默认参数，但是在使用命令时没传入对应的参数值会报错：<code>error: option '-a, --argu-test <name>' argument missing</code>。</p>
</blockquote>
<p>我们还可以在上面代码的option选项的第三个参数位置传入默认值，如下：</p>
<pre><code class="copyable">option('-a, --argu-test <name>', 'test option function -- agru test', 'default value')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的话，我们直接执行代码，不带入任何命令和参数，执行<code>node xxx.js</code>，则会输出<code>output: default value</code>。</p>
<h4 data-id="heading-9">取反命令</h4>
<p>在你的命令前面加上<code>--no</code>代表紧跟的这个命令的反面。</p>
<pre><code class="copyable">program.option('--no-opposite', 'test --no options') // 取反

program.parse(process.argv);

if(program.opposite) &#123;
  console.log('this is a word');
&#125; else &#123;
  console.log('this is a other word');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上面的代码，我们在执行这部分代码不加任何参数的话，默认情况下<code>program.opposite</code>为<code>true</code>。则输出<code>this is a word</code>。如果我们执行时带上参数<code>--no-opposite</code>，则会输出<code>this is a other word</code>。</p>
<blockquote>
<p>关于更多的取反解释，请参考：<a href="https://github.com/tj/commander.js/blob/master/Readme_zh-CN.md#%e5%85%b6%e4%bb%96%e7%9a%84%e9%80%89%e9%a1%b9%e7%b1%bb%e5%9e%8b%e5%8f%96%e5%8f%8d%e9%80%89%e9%a1%b9" target="_blank" rel="nofollow noopener noreferrer">github.com/tj/commande…</a></p>
</blockquote>
<h4 data-id="heading-10">自定义选项（函数）</h4>
<p>option()这个方法在选项描述的后面还可以跟上自定义函数和初始值两个参数，如：<code>option(命令，描述，自定义函数，自定义函数的参数的初始或默认值)</code></p>
<p>函数接收两个参数：用户新输入的参数和当前已有的参数。</p>
<pre><code class="copyable">function increaseFunc(value, preValue) &#123;
  return preValue + 2;
&#125;

program.option('-a, --add', 'add function', increaseFunc, 100);

program.parse(process.argv);

if(program.add > 100) &#123;
  console.log(`current value: $&#123;program.add&#125;`)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行上面的代码<code>node xxx.js -a</code>, 输出102，执行<code>node xxx.js -a -a</code>, 输出104。</p>
<h4 data-id="heading-11">变长参数</h4>
<p>略</p>
<blockquote>
<p>地址：<a href="https://github.com/tj/commander.js/blob/master/Readme_zh-CN.md#%E5%8F%98%E9%95%BF%E5%8F%82%E6%95%B0%E9%80%89%E9%A1%B9" target="_blank" rel="nofollow noopener noreferrer">github.com/tj/commande…</a></p>
</blockquote>
<h3 data-id="heading-12">requiredOption()</h3>
<p>这个表示设置的选项为必填，其参数的写法与<code>option()</code>一样。举个例子</p>
<pre><code class="copyable">program
  .requiredOption('-a, --add <type>', 'add type must have be selected');
  
program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这个段代码，在你执行时必须传入对应的type参数，否则命令就会报错。</p>
<h3 data-id="heading-13">command()</h3>
<p>通过<code>command()</code>可以配置命令，比如我们用的vue cli的<code>create</code> <code>add</code>这些命令就是由<code>command()</code>来处理的。</p>
<h4 data-id="heading-14">参数</h4>
<ul>
<li>配置命令名称及参数，command('命令名 <必填参数> [可选参数]')，如：<code>command('create <name> [options]')</code>。</li>
<li>配置选项，可选。配置noHelp、isDefault这些参数。当opts.noHelp设置为true时，该命令不会打印在帮助信息里。当opts.isDefault设置为true时，若没有指定其他子命令，则会默认执行这个命令。如：<code>command('create <name> [options]', &#123; noHelp: true, isDefault: true &#125;)</code>。</li>
</ul>
<h4 data-id="heading-15">声明可变参数</h4>
<p>在参数名后加上<code>...</code>来声明可变参数，且只有最后一个参数支持这种用法。</p>
<pre><code class="copyable">// 声明可变参数，可变参数会以数组的形式传递给处理函数。
program.command('start <name> [options...]')
  .action((name, options) => &#123;
    console.log(name);
    console.log(options);
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行上述代码<code>node xxx.js start test argumrnt</code>, 对应输出为：</p>
<pre><code class="copyable">test
[ 'argument' ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行上述代码<code>node xxx.js start test argumrnt 1 2 3</code>, 对应输出为：</p>
<pre><code class="copyable">test
[ 'argument', '1', '2', '3' ]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">description()</h3>
<p>用来描述命令的一些提示、说明性的语句，我们在使用help命令时会打印出这些相关的描述</p>
<h4 data-id="heading-17">参数</h4>
<ul>
<li>描述语句，如：<code>description('create a proj')</code>。</li>
</ul>
<h3 data-id="heading-18">action()</h3>
<p>自定义命令执行后的回调函数。</p>
<h4 data-id="heading-19">参数</h4>
<ul>
<li>回调函数，包含的参数是可变的，比如说，你的命令没有定义可选和必选参数，则这个回调函数的第一个参数就是commander对象，否则依次往后推，回调函数最后的参数就是commander对象。比如下面代码：</li>
</ul>
<pre><code class="copyable">program.command('start')
  .description('start a commander')
  .action((cmd) => &#123;
    console.log(cmd); // 输出commander对象信息
  &#125;)

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行上面这个代码<code>node xxx.js start</code>，console输出commander对象。</p>
<pre><code class="copyable">program.command('start <name>')
  .description('start a commander')
  .action((name, cmd) => &#123;
    console.log(name); // 输出name
    console.log(cmd); // 输出commander对象信息
  &#125;)

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">program.command('start <name> [options]')
  .description('start a commander')
  .action((name, options, cmd) => &#123;
    console.log(name); // 输出name
    console.log(options); // 输出name
    console.log(cmd); // 输出commander对象信息
  &#125;)

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">arguments()</h3>
<p>通过<code>arguments</code>可以为最顶层命令指定参数。如下代码：</p>
<pre><code class="copyable">// 直接引用官方代码
program
  .version('0.0.1')
  .arguments('<cmd> [env]')
  .description('test command')
  .action(function(cmdValue, envValue) &#123;
    console.log('command:', cmdValue);
    console.log('environment:', envValue || 'no environment given');
  &#125;);


program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到上面代码，<code>arguments</code>里面声明了一个可选参数，一个必选参数，当我们执行<code>node xxx.js start dev</code>，则对应输出的<code>command: start environment: dev</code>，执行<code>node xxx.js build production</code>，则对应输出的<code>command: build environment: production</code>。其实<code>arguments</code>这个理解为匹配全局命令的一个声明就可以了。</p>
<h3 data-id="heading-21">其他</h3>
<p>到这里，基本上常用的语法就基本完成了，在官方文档上还包含一些其他知识，比如<strong>独立的可执行（子）命令</strong>、<strong>自定义帮助</strong>、<strong>自定义事件监听</strong>等，这里不再赘述了，如果需要了解，请移步官方文档查看：<a href="https://github.com/tj/commander.js/blob/master/Readme_zh-CN.md" target="_blank" rel="nofollow noopener noreferrer">github.com/tj/commande…</a></p>
<h1 data-id="heading-22">最后</h1>
<p>通过前面的命令学习，接下来可以书写一个可运行的完整命令来进行操作</p>
<pre><code class="copyable">const &#123; program &#125; = require('commander');

program
  .version('1.0.0', '-v, --vers')
  .command('start <name> [options...]')
  .description('Test a whole commander order')
  .option('-e --extra [exargs]', 'Test a options')
  .action((name, startOptions, cmd) => &#123;
    // 如果你的可选参数是空的，那么这地方startOptions输出的是空数组
    // console.log(name, startOptions, cmd);
    if(cmd.extra) &#123;
      console.log(`cmd.extra's value is $&#123; cmd.extra &#125;`);
    &#125; else &#123;
      console.log('no cmd.extra');
    &#125;
    if(startOptions.length > 0) &#123;
      startOptions.forEach(function(item) &#123;
        console.log(item);
      &#125;)
    &#125;
  &#125;)

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码我命名为commander-final.js。然后执行以下命令：</p>
<ul>
<li>node commander-final.js -vers</li>
</ul>
<pre><code class="copyable">1.0.0
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>node commander-final.js -h</li>
</ul>
<pre><code class="copyable">Usage: commander-final [options] [command]

Options:
  -v, --vers                           output the version number
  -h, --help                           display help for command

Commands:
  start [options] <name> [options...]  Test a whole commander order
  help [command]                       display help for command

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>node commander-final.js start -h</li>
</ul>
<pre><code class="copyable">Usage: commander-final start [options] <name> [options...]

Test a whole commander order

Options:
  -e --extra [exargs]  Test a options
  -h, --help           display help for command

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>node commander-final.js start mycli dev producrion -e hash</li>
</ul>
<pre><code class="copyable">cmd.extra's value is hash
dev
producrion
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面就是对应的命令输出的学习。</p>
<p>到这儿commander入门就算结束了，如有疏漏或错误还请大家多多指教！也欢迎大家关注我的公众号：程序曲奇饼！</p></div>  
</div>
            