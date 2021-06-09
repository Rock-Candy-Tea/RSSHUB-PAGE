
---
title: 'js实现解数独游戏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9cad4cdafbf4658a1d1cd26a44b4b33~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 00:21:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9cad4cdafbf4658a1d1cd26a44b4b33~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第4天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<div class="notranslate"><p>编写一个程序，通过填充空格来解决数独问题。</p>
<p>数独的解法需<strong> 遵循如下规则</strong>：</p>
<ol>
<li>数字 <code>1-9</code> 在每一行只能出现一次。</li>
<li>数字 <code>1-9</code> 在每一列只能出现一次。</li>
<li>数字 <code>1-9</code> 在每一个以粗实线分隔的 <code>3x3</code> 宫内只能出现一次。（请参考示例图）</li>
</ol>
<p>数独部分空格内已填入了数字，空白格用 <code>'.'</code> 表示。</p>
<p> </p>
<div class="top-view__1vxA">
<div class="original__bRMd">
<div>
<p><strong>示例：</strong></p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9cad4cdafbf4658a1d1cd26a44b4b33~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<pre><strong>输入：</strong>board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
<strong>输出：</strong>[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
<strong>解释：</strong>输入的数独如上图所示，唯一有效的解决方案如下所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/971231b5d897489cb781e4bf73f660b0~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
</pre>
<p> </p>
<p><strong>提示：</strong></p>
<ul>
<li><code>board.length == 9</code></li>
<li><code>board[i].length == 9</code></li>
<li><code>board[i][j]</code> 是一位数字或者 <code>'.'</code></li>
<li>题目数据 <strong>保证</strong> 输入数独仅有一个解</li>
</ul>
</div>
</div>
</div>
</div>
<h1 data-id="heading-0">解法</h1>
<h2 class="css-18ck646-title-Title es0hbuf2" data-id="heading-1">递归 + 回溯 + 位运算</h2><div class="css-1o4ejbc-Row2 es0hbuf3"><a href="https://juejin.cn/u/zoffer/"><div class="css-fndr66-UsernameContainer e123u7vb0"><span class="css-x7m7pv-NameWrap e123u7vb1">Zoffer</span><span class="e123u7vb3 css-fmw0cr-ReputationLevelContainer-StyledReputationLevel ekys2oz0"><span class="css-1vu7cyl-Level ekys2oz1">L4</span></span></div></a><span class="css-1407w2u-PublishDate es0hbuf5">发布于 2020-06-23</span><span class="css-1o2blet-HitCount es0hbuf6">1.4k</span><a class="es0hbuf7 css-1ad4xj5-BasicTag-StyledTag e4dtce60" href="https://juejin.cn/tag/bit-manipulation/"><span>位运算</span></a><a class="es0hbuf7 css-1ad4xj5-BasicTag-StyledTag e4dtce60" href="https://juejin.cn/tag/recursion/"><span>递归</span></a><a class="es0hbuf7 css-1ad4xj5-BasicTag-StyledTag e4dtce60" href="https://juejin.cn/tag/backtracking/"><span>回溯算法</span></a><a class="es0hbuf7 css-1ad4xj5-BasicTag-StyledTag e4dtce60" href="https://juejin.cn/topic/javascript/"><span>JavaScript</span></a></div><div class="css-1jiyb8u-ContentContainer e1ak08xt0"><div class="e1ak08xt1 css-154e5au-StyledRenderedMarkdown"><h3 data-id="heading-2">递归</h3>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9d16f6344494523a03b6bd30aab66e9~tplv-k3u1fbpfcp-zoom-1.image" alt="sudoku.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>每次选取<strong>可填数字最少</strong>的空格，试探次数更少，发现错误更快。</li>
</ul>
<h3 data-id="heading-3">位运算</h3>
<ul>
<li>使用 9-bit 保存数字 1~9 的占用情况，通过位运算处理，更加轻松高效。</li>
</ul>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7705da1f6b04445905f1ea63f02468a~tplv-k3u1fbpfcp-zoom-1.image" alt="250px-Sudoku-by-L2G-20050714.png" loading="lazy" referrerpolicy="no-referrer"></p>
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>9</th>
<th>8</th>
<th>7</th>
<th>6</th>
<th>5</th>
<th>4</th>
<th>3</th>
<th>2</th>
<th>1</th>
</tr>
</thead>
<tbody>
<tr>
<td>行</td>
<td>r = rows[5]</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>列</td>
<td>c = columns[3]</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>3x3方格</td>
<td>b = boxs[1][1]</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>或运算</td>
<td>x = r | c | b</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>取反 9-bit</td>
<td>p = x ^ 0b111111111</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>截取最低位 1</td>
<td>s = -p & p</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>清除截取的位</td>
<td>p ^ s</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>
<h3 data-id="heading-4">代码</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;character[][]&#125;</span> <span class="hljs-variable">board</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;void&#125;</span> </span>Do not return anything, modify board in-place instead.
 */</span>
<span class="hljs-keyword">var</span> solveSudoku = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">board</span>) </span>&#123;
    <span class="hljs-keyword">new</span> Sudoku(board).solve();
&#125;;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Sudoku</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">board</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.board = board;
        <span class="hljs-comment">//行</span>
        <span class="hljs-built_in">this</span>.rows = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">9</span>).fill(<span class="hljs-number">0</span>);
        <span class="hljs-comment">//列</span>
        <span class="hljs-built_in">this</span>.columns = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">9</span>).fill(<span class="hljs-number">0</span>);
        <span class="hljs-comment">//3x3方格</span>
        <span class="hljs-built_in">this</span>.boxs = <span class="hljs-built_in">Array</span>.from(&#123; <span class="hljs-attr">length</span>: <span class="hljs-number">3</span> &#125;, <span class="hljs-function">() =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">3</span>).fill(<span class="hljs-number">0</span>));
        <span class="hljs-comment">//未填空格</span>
        <span class="hljs-built_in">this</span>.emptyCells = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
    &#125;
    <span class="hljs-function"><span class="hljs-title">solve</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">//初始化已知的数字</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">9</span>; i++) &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < <span class="hljs-number">9</span>; j++) &#123;
                <span class="hljs-keyword">let</span> num = <span class="hljs-built_in">this</span>.board[i][j];
                <span class="hljs-keyword">if</span> (num !== <span class="hljs-string">"."</span>) &#123;
                    <span class="hljs-comment">//将数字转化为二进制标记</span>
                    <span class="hljs-comment">//1 -> 0b1, 2 -> 0b10, 3 -> 0b100, 4 -> 0b1000 ...</span>
                    <span class="hljs-keyword">const</span> sign = <span class="hljs-number">1</span> << (<span class="hljs-built_in">Number</span>(num) - <span class="hljs-number">1</span>);
                    <span class="hljs-built_in">this</span>.rows[i] |= sign;
                    <span class="hljs-built_in">this</span>.columns[j] |= sign;
                    <span class="hljs-built_in">this</span>.boxs[<span class="hljs-built_in">Math</span>.floor(i / <span class="hljs-number">3</span>)][<span class="hljs-built_in">Math</span>.floor(j / <span class="hljs-number">3</span>)] |= sign;
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-built_in">this</span>.emptyCells.add((i << <span class="hljs-number">4</span>) | j);
                &#125;
            &#125;
        &#125;
        <span class="hljs-comment">//主逻辑</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.fillNext();
    &#125;
    <span class="hljs-function"><span class="hljs-title">fillNext</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> cellInfo = <span class="hljs-built_in">this</span>.getEmptyCell();
        <span class="hljs-keyword">if</span> (cellInfo === <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-comment">//没有空格，解题成功</span>
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;
        <span class="hljs-keyword">let</span> [i, j, possible] = cellInfo;
        <span class="hljs-keyword">while</span> (possible) &#123;
            <span class="hljs-comment">//截取其中一个可能性</span>
            <span class="hljs-keyword">const</span> sign = -possible & possible;
            <span class="hljs-comment">//填入空格</span>
            <span class="hljs-built_in">this</span>.fillCell(i, j, sign);
            <span class="hljs-comment">//继续下一个填充</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.fillNext()) &#123;
                <span class="hljs-comment">//填充成功</span>
                <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">//排除当前数字</span>
                possible ^= sign;
                <span class="hljs-comment">//清空空格</span>
                <span class="hljs-built_in">this</span>.cleanCell(i, j, sign);
            &#125;
        &#125;
        <span class="hljs-comment">//穷尽所有可能性，回溯</span>
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;
    <span class="hljs-function"><span class="hljs-title">getEmptyCell</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> min = <span class="hljs-number">10</span>;
        <span class="hljs-keyword">let</span> cellInfo = <span class="hljs-literal">null</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> id <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.emptyCells) &#123;
            <span class="hljs-keyword">const</span> i = id >> <span class="hljs-number">4</span>, j = id & <span class="hljs-number">0b1111</span>;
            <span class="hljs-keyword">const</span> possible = <span class="hljs-built_in">this</span>.getCellPossible(i, j);
            <span class="hljs-keyword">const</span> count = <span class="hljs-built_in">this</span>.countPossible(possible);
            <span class="hljs-keyword">if</span> (min > count) &#123;
                <span class="hljs-comment">//挑选可能性最少的格子，理论上可减少犯错回溯</span>
                cellInfo = [i, j, possible];
                min = count;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> cellInfo;
    &#125;
    <span class="hljs-function"><span class="hljs-title">countPossible</span>(<span class="hljs-params">possible</span>)</span> &#123;
        <span class="hljs-comment">//计算二进制 1 的数量</span>
        <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
        <span class="hljs-keyword">while</span> (possible) &#123;
            possible &= (possible - <span class="hljs-number">1</span>);
            count++;
        &#125;
        <span class="hljs-keyword">return</span> count;
    &#125;
    <span class="hljs-function"><span class="hljs-title">fillCell</span>(<span class="hljs-params">i, j, sign</span>)</span> &#123;
        <span class="hljs-comment">//对应位变成1，标记占用</span>
        <span class="hljs-built_in">this</span>.rows[i] |= sign;
        <span class="hljs-built_in">this</span>.columns[j] |= sign;
        <span class="hljs-built_in">this</span>.boxs[<span class="hljs-built_in">Math</span>.floor(i / <span class="hljs-number">3</span>)][<span class="hljs-built_in">Math</span>.floor(j / <span class="hljs-number">3</span>)] |= sign;
        <span class="hljs-comment">//填入空格</span>
        <span class="hljs-built_in">this</span>.emptyCells.delete((i << <span class="hljs-number">4</span>) | j);
        <span class="hljs-built_in">this</span>.board[i][j] = <span class="hljs-built_in">String</span>(<span class="hljs-built_in">Math</span>.log2(sign) + <span class="hljs-number">1</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-title">cleanCell</span>(<span class="hljs-params">i, j, sign</span>)</span> &#123;
        <span class="hljs-comment">//对应位变为0，清除占用</span>
        <span class="hljs-built_in">this</span>.rows[i] &= ~sign;
        <span class="hljs-built_in">this</span>.columns[j] &= ~sign;
        <span class="hljs-built_in">this</span>.boxs[<span class="hljs-built_in">Math</span>.floor(i / <span class="hljs-number">3</span>)][<span class="hljs-built_in">Math</span>.floor(j / <span class="hljs-number">3</span>)] &= ~sign;
        <span class="hljs-comment">//清空格子</span>
        <span class="hljs-built_in">this</span>.emptyCells.add((i << <span class="hljs-number">4</span>) | j)
        <span class="hljs-built_in">this</span>.board[i][j] = <span class="hljs-string">"."</span>;
    &#125;
    <span class="hljs-function"><span class="hljs-title">getCellPossible</span>(<span class="hljs-params">i, j</span>)</span> &#123;
        <span class="hljs-comment">//获取格子可能的取值，二进制1表示可选</span>
        <span class="hljs-keyword">return</span> (<span class="hljs-built_in">this</span>.rows[i] | <span class="hljs-built_in">this</span>.columns[j] | <span class="hljs-built_in">this</span>.boxs[<span class="hljs-built_in">Math</span>.floor(i / <span class="hljs-number">3</span>)][<span class="hljs-built_in">Math</span>.floor(j / <span class="hljs-number">3</span>)]) ^ <span class="hljs-number">0b111111111</span>;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div></div></div>  
</div>
            