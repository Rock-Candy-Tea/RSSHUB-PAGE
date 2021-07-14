
---
title: '学习笔记之JS正则'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1009'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 04:00:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=1009'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<ul>
<li>以下内容均来自<code>老姚</code>的<a href="https://juejin.cn/post/6844903487155732494" target="_blank" title="https://juejin.cn/post/6844903487155732494">JS正则表达式完整教程（略长）</a>.</li>
<li>文本仅为学习摘录.</li>
</ul>
<h2 data-id="heading-1">正则知识架构</h2>
<ul>
<li>字符匹配
<ol>
<li>两种模糊匹配
<ul>
<li>横向模糊匹配: 匹配一个长度不确定的分组或者字符</li>
<li>纵向模糊匹配: 匹配一个不确定内容的字符</li>
</ul>
</li>
<li>字符组
<ul>
<li>字符组(字符类),用以实现纵向模糊匹配.</li>
<li>意义是匹配字符组中的字符之一.</li>
<li>案例: <code>[abc]</code>表示匹配"a""b""c"其中之一.</li>
<li>由于"-"在字符组中可以连接两个字符表示连续的字符序列,所以我们需要注意转义.如:
<ul>
<li><code>[-az]</code>或<code>[az-]</code>或<code>[a\-z]</code>.</li>
</ul>
</li>
</ul>
</li>
<li>量词
<ul>
<li>量词,用以实现横向模糊匹配.</li>
<li>意义是描述字符或者分组的重复出现次数.</li>
<li>量词的匹配模式分为:<code>贪婪模式</code>和<code>惰性模式</code>:
<ul>
<li>贪婪模式(默认): 在量词区间内,尽可能多匹配.</li>
<li>惰性模式: 在量词区间内,尽可能少匹配.
<ul>
<li>开启:在量词后面加<code>?</code>.</li>
<li>注意:这个<code>?</code>是修饰量词的.</li>
</ul>
</li>
<li>贪婪量词: <code>&#123;m,n&#125;</code>.</li>
<li>惰性量词: <code>&#123;m,n&#125;?</code>.</li>
</ul>
</li>
</ul>
</li>
<li>分支结构
<ul>
<li>支持多个子模式任选其一,使用<code>|</code>(管道符)分隔多个子模式.</li>
<li>注意分支结构内部内容使用<code>()</code>与外部分离,如:<code>(p1|p2|p3)</code>.</li>
<li>分支结构中的匹配优先级: 从前往后.
<ul>
<li>比如我用<code>/good|goodbye/</code>，去匹配"goodbye"字符串时，结果是"good".</li>
</ul>
</li>
</ul>
</li>
</ol>
</li>
<li>位置匹配
<ol>
<li>什么是位置?
<ul>
<li>相邻字符之间的位置.</li>
</ul>
</li>
<li>如何匹配位置?
<ul>
<li>使用字符锚.</li>
</ul>
</li>
<li>位置的特性
<ul>
<li>对于位置的理解,我们可以理解空字符"",如:介于字符之间,介于开头结尾之间.</li>
<li>直观展示:
<ul>
<li><code>"hello" == "" + "h" + "" + "e" + "" + "l" + "" + "l" + "o" + ""</code></li>
</ul>
</li>
</ul>
</li>
</ol>
</li>
<li>括号的作用
<ol>
<li>分组与分支结构
<ul>
<li>用括号隔离分组内容和外部内容,如<code>/(ab)+/g</code>.</li>
<li>用括号隔离分支结构内部内容与外部内容,如<code>(p1|p2)</code>.</li>
</ul>
</li>
<li>捕获分组
<ul>
<li>我们可以用<code>$n</code>捕获分组.</li>
</ul>
</li>
<li>反向引用
<ul>
<li>使用<code>\1</code>反向引用分组.</li>
<li>如果没有则翻译成转义字符.</li>
</ul>
</li>
<li>非捕获分组
<ul>
<li>不可被捕获,无法反向引用,表达方式<code>(?:p)</code>.</li>
</ul>
</li>
</ol>
</li>
<li>回溯法原理
<ol>
<li>没有回溯的匹配
<ul>
<li>假设: 用<code>/ab&#123;1,3&#125;c/</code>去匹配<code>"abbbc"</code>则不会发生回溯.</li>
</ul>
</li>
<li>有回溯的匹配
<ul>
<li>假设: 用<code>/ab&#123;1,3&#125;c/</code>去匹配<code>"abbc"</code>则不会发生回溯.</li>
<li>本质上是由<code>贪婪模式</code>的特性引起的.</li>
<li>解决方案:
<ol>
<li>使用惰性模式(当然惰性模式中也会有溯回).</li>
<li>使用<code>[^"]</code>(假设匹配引号内部的内容),排除边界字符.</li>
</ol>
</li>
</ul>
</li>
<li>常见的回溯形式
<ul>
<li>我们知道:在<code>深度优先搜索算法</code>中,<code>退回到之前某一步</code>的这个过程,我们将其称为<code>回溯</code>.</li>
<li>即,<code>也就是尝试匹配失败时,接下来的一步通常就是回溯</code>.</li>
<li><code>贪婪量词</code>,<code>惰性量词</code>,<code>分支结构</code>这三个场景都会存在溯回.因为都属于暧昧的表达方式.</li>
</ul>
</li>
</ol>
</li>
<li>拆分
<ol>
<li>结构和操作符
<ul>
<li>字符字面量.</li>
<li>字符组.</li>
<li>量词.</li>
<li>锚字符.</li>
<li>分组.</li>
<li>选择分支.</li>
<li>反向引用.</li>
</ul>
</li>
<li>注意要点
<ul>
<li>匹配字符串整体问题,如:<code>/^abc|bcd$/</code>(匹配不符合预期)=><code>/^(abc|bcd)$/</code>.</li>
<li>量词连缀问题,如:<code>/[abc]&#123;3&#125;+/</code>(不合法)=><code>/([abc]&#123;3&#125;)+/</code>.</li>
<li>元字符转义问题,如:<code>"^$.*+?|\\/[]&#123;&#125;=!:-,"</code>对应的正则<code>/\^\$\.\*\+\?\|\\\/\[\]\&#123;\&#125;\=\=\!\:\-\,/</code>
<ul>
<li>元字符一律可以转义.</li>
<li>字符组中必要转义,如<code>[]</code>,<code>^</code>,<code>-</code>,</li>
<li>简要转义<code>/\[abc\]/</code>=><code>/\[abc]/</code>(两者等价),<code>/\&#123;3,5&#125;/</code>同理.</li>
<li><code>&#123;,n&#125;</code>是一个不合法的量词,会被当做普通字符串(换言之,不用转义).</li>
<li><code>=</code>,<code>+</code>,<code>:</code>,<code>-</code>,<code>,</code>等符号,只要不在特殊结构中,也不需要转义.</li>
<li>括号前后都需要转移的,如<code>/\(123\)/</code>.</li>
<li><code>^</code>,<code>$</code>,<code>.</code>,<code>*</code>,<code>+</code>,<code>?</code>,<code>|</code>,<code>\</code>,<code>/</code>等字符,只要不在字符组内,都需要转义的.</li>
</ul>
</li>
</ul>
</li>
</ol>
</li>
<li>构建(方法论)
<ol>
<li>平衡法则.
<ul>
<li>匹配预期的字符串.</li>
<li>不匹配非预期的字符串.</li>
<li>可读性和可维护性.</li>
<li>效率.</li>
</ul>
</li>
<li>构建正则前提.
<ul>
<li>能否使用正则.</li>
<li>是否有必要使用使用正则.如:
<ul>
<li>拆分字符串可以使用<code>split</code>代劳.</li>
<li>判断是否存在某字符使用<code>search,indexOf</code>代劳.</li>
</ul>
</li>
<li>是否有必要构建一个复杂的正则
<ul>
<li>对于<code>选择分支</code>,我们可以使用<code>js条件语句</code>代劳.以拆分正则.</li>
</ul>
</li>
</ul>
</li>
<li>准确性.
<ul>
<li>匹配预期的字符串.</li>
<li>不匹配非预期的字符串.</li>
</ul>
</li>
<li>效率.
<ul>
<li>优化方式:
<ul>
<li>使用具体型字符来代替通配符,来消除回溯.</li>
<li>使用非捕获型分组.</li>
<li>独立出确定字符.</li>
<li>提取分支公共部分.</li>
<li>减少分支数量,缩小它们的范围.</li>
</ul>
</li>
</ul>
</li>
</ol>
</li>
<li>编译
<ol>
<li>正则表达式的四种操作
<ul>
<li>分别有:<code>验证</code>,<code>切分</code>,<code>提取</code>,<code>替换</code>.</li>
<li><code>验证</code>: 换言之,就是需要返回一个<code>boolean</code>.
<ul>
<li><code>search</code>: 通过将返回的哨位值<code>-1</code>转换成<code>0</code>,再<code>!!</code>转成<code>boolean</code>.</li>
<li><code>test</code>: 通过返回的<code>boolean</code>判定(如果没有<code>^</code>和<code>$</code>限定,则存在即可).</li>
<li><code>match</code>: 返回值有两种可能一种是<code>null</code>,另一种是数组,可以直接<code>!!</code>转换成<code>boolean</code>.</li>
<li><code>exec</code>: 和<code>match</code>同理.</li>
</ul>
</li>
<li><code>切分</code>: 按照一定的规则切分字符串.
<ul>
<li><code>split</code>: 如,<code>2017/06/26".split(/\D/)</code>.</li>
</ul>
</li>
<li><code>提取</code>: 使用分组捕获功能,提取部分匹配的数据.
<ul>
<li><code>match</code>: 通过返回的数据提取.
<ul>
<li>数据结构: <code>[match,$1,$2,$3,index:_index,input:_input]</code>.</li>
</ul>
</li>
<li><code>exec</code>: 与<code>match</code>同理.</li>
<li><code>test</code>: 调用<code>test</code>之后,通过构造函数属性<code>RegExp.$1</code>,<code>RegExp.$2</code>...获取.</li>
<li><code>search</code>: 与<code>test</code>同理.</li>
<li><code>replace</code>: 通过<code>Array.prototype.push</code>抛出要提取的数据.</li>
</ul>
</li>
<li><code>替换</code>: 替换匹配字符.
<ul>
<li><code>replace</code>: 把日期的横杠换成斜杠(把横杠换成斜杠的原因就是,我们需要<code>new</code>一个日期).</li>
</ul>
</li>
</ul>
</li>
<li>相关API注意要点
<ul>
<li>明确API的所属对象,如:
<ul>
<li><code>search,split,match,replace</code>: 属于字符串(String#)实例方法.</li>
<li><code>test,exec</code>: 属于正则(RegExp#)实例方法.</li>
</ul>
</li>
<li>注意参数问题,如:
<ul>
<li>字符串4个实例方法,即<code>search</code>,<code>split</code>,<code>match</code>,<code>replace</code>都支持正则和字符串.</li>
<li><code>search</code>和<code>match</code>: 会把字符串直接转换为正则,也就是说,有必要的时候我们需要进行转义.</li>
<li><code>split</code>和<code>replace</code>: 则会作为字面量自动转义,也就是说,没有必要进行手动转义.</li>
</ul>
</li>
<li><code>match</code>和<code>exec</code>之间的不同:
<ul>
<li>不带<code>g</code>的情况下,<code>match</code>和<code>exec</code>都会返回完整的匹配信息.</li>
<li>带<code>g</code>的情况下:
<ul>
<li><code>match</code>: 会将所有完整正则匹配的内容返回,但是不会返回完整信息.</li>
<li><code>exec</code>: 每调用一次会返回一条完整信息,依次推移,我们通过<code>RegExp.lastIndex</code>获取到下一次开始的位置,如果是<code>0</code>,我们就停止.(while).</li>
</ul>
</li>
<li>引申<code>test</code>和<code>exec</code>一样,带<code>g</code>之后,如果调用多次,就会RegExp.lastIndex推移,而且test最后的返回值肯定是<code>false</code>.</li>
</ul>
</li>
<li><code>test</code>整体匹配需要<code>^</code>和<code>$</code>.</li>
<li><code>split</code>:
<ul>
<li>第二个参数决定返回数组的最大长度.</li>
<li>如果正则是加入分组<code>/(,)/</code>,则结果包含分隔符<code>["999",",","999",",","999"]</code>.</li>
</ul>
</li>
<li><code>replace</code>:
<ul>
<li>当replace第二个参数是字符串的时候,如下字符有特殊的含义.
<ul>
<li><code>$1</code>,<code>$2</code>,...,<code>$99</code>匹配第1~99个分组里捕获的文本</li>
<li><code>$&</code>匹配到的子串文本</li>
<li><code>$\</code>匹配到的子串的左边文本</li>
<li><code>$'</code>匹配到的子串的右边文本</li>
<li><code>?</code>美元符号</li>
</ul>
</li>
<li>当replace的第二个参数是函数的时候,其回调函数传入这些值:
<ul>
<li><code>(match,$1,$2,$3,index,input)</code>.</li>
</ul>
</li>
<li>replace带<code>g</code>调用多次的时候会出现index偏移的效果.</li>
</ul>
</li>
<li>不推荐使用构造函数,推荐使用字面量,省代码.且不执行的时候更为轻量级.</li>
<li>修饰符
<ul>
<li>ES5中修饰符,共3个:
<ol>
<li><code>g</code>(global):全局匹配.</li>
<li><code>i</code>(ignoreCase):忽略大小写.</li>
<li><code>m</code>(multiline):多行匹配,只影响<code>^</code>和<code>$</code>,两者将会变成行开头和行结尾.</li>
</ol>
</li>
</ul>
</li>
<li>正则实例对象的只读属性.
<ul>
<li><code>regex.global</code>: 是否为全局配.</li>
<li><code>regex.ignoreCase</code>: 是否忽略大小写.</li>
<li><code>regex.multiline</code>: 是否为多行匹配.</li>
<li><code>regex.lastIndex</code>: 下一个开始匹配的位置.</li>
<li><code>regex.source</code>: 获取构造函数构造出来的成品的字符串.如:<code>"(^|\\s)high(\\s|$)"</code>.</li>
</ul>
</li>
<li>构造函数的静态属性.
<ul>
<li><code>RegExp.input</code>: 最近一次目标字符串,简写<code>RegExp["$_"]</code>.</li>
<li><code>RegExp.lastMatch</code>: 最近一次匹配的文本,简写<code>RegExp["$&"]</code>.</li>
<li><code>RegExp.lastParen</code>: 最近一次捕获的文本,简写<code>RegExp["$+"]</code>.</li>
<li><code>RegExp.leftContext</code>: 目标字符串中lastMatch之前的文本,简写成<code>RegExp["$</code>"]``.</li>
<li><code>RegExp.rightContext</code>: 目标字符串中lastMatch之后的文本,简写成<code>RegExp["$'"]</code>.</li>
</ul>
</li>
</ul>
</li>
</ol>
</li>
</ul>
<h2 data-id="heading-2">归类</h2>
<h3 data-id="heading-3">常见字符组简写形式</h3>
<ul>
<li><code>\d</code>(digit)就是<code>[0-9]</code>:匹配数字字符.</li>
<li><code>\D</code>就是<code>[0-9]</code>:匹配除了数字以外的任意字符.</li>
<li><code>\w</code>(word)就是<code>[0-9A-Za-z_]</code>: 匹配单词字符,包括:数字,大小写字母,下划线.</li>
<li><code>\W</code>就是<code>[^0-9A-Za-z_]</code>:匹配非单词字符.</li>
<li><code>\s</code>(space character)就是<code>[\t\v\n\r\f]</code>匹配空白符,包括:空格,水平制表符,垂直制表符,换行符,回车符,换页符.</li>
<li><code>\S</code>就是<code>[\t\v\n\r\f]</code>匹配非空白符.</li>
<li><code>.</code>就是<code>[^\n\r\u2028\u2029]</code>,通配符,几乎匹配任意字符,除了:换行符,回车符,行分隔符,段分隔符.</li>
<li>如果需要匹配任意字符,则需要:<code>[\d\D]</code>,<code>[\w\W]</code>,<code>[\s\S]</code>,<code>[^]</code></li>
</ul>
<h3 data-id="heading-4">常见量词简写形式</h3>
<ul>
<li><code>&#123;m,&#125;</code>:匹配至少出现m次.</li>
<li><code>&#123;m&#125;</code>:等价于<code>&#123;m,m&#125;</code>,表示出现m次.</li>
<li><code>?</code>:等价于<code>&#123;0,1&#125;</code>,表示出现1次或没有出现.</li>
<li><code>+</code>:等价于<code>&#123;1,&#125;</code>,表示至少出现1次.</li>
<li><code>*</code>:等价于<code>&#123;0,&#125;</code>表示可以出现人一次,或者没有出现.</li>
</ul>
<h3 data-id="heading-5">字符锚点</h3>
<blockquote>
<p>在es5中,共有6个锚字符:
^ $ \b \B (?=p) (?!p)</p>
</blockquote>
<ul>
<li><code>^</code>和<code>$</code>:
<ul>
<li><code>^</code>(脱字符),匹配开头.在多行模式中匹配行开头.</li>
<li><code>$</code>(美元符号),匹配结尾,多行模式中匹配行结尾.</li>
</ul>
</li>
<li><code>\b</code>和<code>\B</code>:
<ul>
<li><code>\b</code>指的是单词边界,也就是<code>\w</code>与\W(或^或$)之间.</li>
<li><code>\B</code>指的是非单词边界,也就是<code>\w</code>与<code>\w</code>之间,<code>\W</code>与<code>\W</code>之间,<code>\W</code>与<code>^</code>之间,<code>\W</code>与<code>$</code>之间.</li>
</ul>
</li>
<li><code>(?=p)</code>和<code>(?!p)</code>:
<ul>
<li><code>p</code>指的是一个<code>子模式</code>.</li>
<li><code>(?=p)</code>的学名是<code>正向先行断言</code>(positive lookahead).
<ul>
<li>匹配<code>子模式</code>的前面位置.</li>
</ul>
</li>
<li><code>(?!p)</code>的学名是<code>负向先行断言</code>(negative lookahead).
<ul>
<li>匹配非(<code>子模式</code>的前面位置).</li>
</ul>
</li>
<li><code>(?<=p)</code>的学名是<code>正向后继断言</code>(positive lookbehind).
<ul>
<li>匹配<code>子模式</code>的后面位置.</li>
</ul>
</li>
<li><code>(?<!p)</code>的学名是<code>负向后继断言</code>(negative lookbehind).
<ul>
<li>匹配非(<code>子模式</code>的后面位置).</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-6">表达式结构</h3>
<ul>
<li><code>字面量</code>: 匹配一个具体字符(注意特殊符号转义).</li>
<li><code>字符组</code>: 匹配一个字符的多种可能之一.如:<code>[0-9]</code>,<code>\d</code>.</li>
<li><code>量词</code>: 匹配字符连续出现的次数.</li>
<li><code>锚点</code>: 一个<code>位置</code>,而不是<code>字符</code>.</li>
<li><code>分组</code>: 匹配一个整体,如<code>(ab)+</code>,非捕获<code>(?:ab)+</code>.</li>
<li><code>分支</code>: 匹配多个子表达式之一.</li>
<li><code>反向引用</code>: 引用出现过分组,如<code>\2</code>.</li>
</ul>
<h3 data-id="heading-7">表达式操作符</h3>
<ul>
<li>转义符: <code>\</code>.</li>
<li>括号和方括号: <code>()</code>,<code>(?:)</code>,<code>(?=)</code>,<code>(?!)</code>,<code>[]</code>.</li>
<li>量词限定符: <code>&#123;m&#125;</code>,<code>&#123;m,n&#125;</code>,<code>&#123;m,&#125;</code>,<code>?</code>,<code>*</code>,<code>+</code>.</li>
<li>位置和序列: <code>^</code>,<code>$</code>,<code>\</code>,<code>\元字符</code>,<code>一般字符</code>.</li>
<li>管道符: <code>|</code></li>
</ul>
<h2 data-id="heading-8">案例</h2>
<h3 data-id="heading-9">回溯图</h3>
<ul>
<li>贪婪量词</li>
</ul>
<pre><code class="copyable">var string = "12345";
var regex = /(\d&#123;1,3&#125;)(\d&#123;1,3&#125;)/;
console.log( string.match(regex) );
// => ["12345", "123", "45", index: 0, input: "12345"]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>惰性量词</li>
</ul>
<pre><code class="copyable">var string = "12345";
var regex = /(\d&#123;1,3&#125;?)(\d&#123;1,3&#125;)/;
console.log( string.match(regex) );
// => ["1234", "1", "234", index: 0, input: "12345"]
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">RegExp: /^\d&#123;1,3&#125;?\d&#123;1,3&#125;$/

*__Begin!___Digit___Digit___End!__*
           |_____| |_____|
        1 to 3 times 1 to 3 times
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>分支结构</li>
</ul>
<pre><code class="copyable">RegExp: /^(?:can|candy)$/

            __can__
*__Begin!__|       |__end!__*
           |_candy_|
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">元字符转义测试</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> string = <span class="hljs-string">"^$.*+?|\\/[]&#123;&#125;=!:-,"</span>;
<span class="hljs-keyword">var</span> regex = <span class="hljs-regexp">/\^\$\.\*\+\?\|\\\/\[\]\&#123;\&#125;\=\=\!\:\-\,/</span>
<span class="hljs-built_in">console</span>.log(regex.test(string));
<span class="hljs-comment">// => true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> string = <span class="hljs-string">"^$.*+?|\\/[]&#123;&#125;=!:-,"</span>
<span class="hljs-keyword">var</span> stirng2 = <span class="hljs-string">"\^\$\.\*\+\?\|\\\/\[\]\&#123;\&#125;\=\!\:\-\,"</span>
<span class="hljs-built_in">console</span>.log(string === string2)
<span class="hljs-comment">// => true</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            