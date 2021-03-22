
---
title: 如何在Windows环境下写一个控制台文本编辑器
categories: 
    - 社交媒体
    - 知乎 - 用户文章
author: 知乎 - 用户文章
comments: false
date: Mon, 19 Jan 1970 10:51:32 GMT
thumbnail: ''
---

<div>   
<blockquote> 从高中毕业就开始研究Editor，想写一个自己的文本编辑器。 大一时不了解其他东西就想用控制台写一个，留下了这么一个不完备的多行输入函数。<br> </blockquote><h2><b>1. 准备</b></h2><p>在尝试实现这个函数的过程中，我试过<code>printf()</code>系列，也试过<code>getchar()</code>系列，还有<code>getch()</code>系列……后来发现回车入栈函数并不能满足多行文本输入的需求，最后找到了<code>_getch()</code>与<code>_putch()</code>。由于<code>char</code>类型不能容纳中文（2个字节），选择了<code>wchar_t</code>作为储存字符的类型，与之相匹配的函数是<code>void _putwch(wchar_t c)</code>与<code>wchar_t _getwch()</code>。</p><p>现在可以很容易实现输入一个字符并输出：</p><div class="highlight"><pre><code class="language-c"><span class="n">wchar_t</span> <span class="n">ch</span> <span class="o">=</span> <span class="n">_getwch</span><span class="p">();</span>
<span class="n">_putwch</span><span class="p">(</span><span class="n">ch</span><span class="p">);</span></code></pre></div><h2><b>2. 架构</b></h2><h3><b>2.1. 基本数据结构</b></h3><ul><li>Edit box config</li></ul><div class="highlight"><pre><code class="language-text">struct EditBoxConfig &#123;
  char *filename;
  short cursor_x, cursor_y;
  short screen_rows, screen_cols;
  struct Word *head_word;
  // Head_word has no characters(WEOF) which follows by the text.
&#125;;</code></pre></div><ul><li>Word<br> 我使用了双向链表来储存输入字符，但也可以尝试<code>char *</code>这样的数组配合<code>malloc</code>和<code>realloc</code>来写，理论上是更好的选择。<br> </li></ul><div class="highlight"><pre><code class="language-text">struct Word &#123;
  wchar_t ch;
  struct Word *last;
  struct Word *next;
&#125;;</code></pre></div><h3><b>2.2. 输入</b></h3><ul><li>输入函数需要正确处理输入的内容：</li></ul><div class="highlight"><pre><code class="language-text">wchar_t ch;
switch (ch = _getwch()) &#123;
    // You can find the number of these characters on the Internet.
    case ARROW_KEY:
        move_pointer(_getwch());
        break;
  case BACKSPACE:
        delete_word();
        break;
  case ...:
        /* You can do what you want.*/
        break; 
  default: /* Word and enter. */
        insert_word(ch);
        break;
&#125;</code></pre></div><ul><li>在输入过程中需要定义一个<code>present_word</code>在储存当前指向的字符。我们可以将它看作虚拟光标。</li></ul><h3><b>2.3. 输出</b></h3><ul><li>输出需要在正确的位置渲染出字符：</li></ul><div class="highlight"><pre><code class="language-text">// This is print word head.
// If the text is beyond the screen, 
// it will not be the head of text.
struct Word *word = word_head;

// Print line by line.
for (i = 0; i < editor.screen_rows - 1; i++) &#123;
    // If current Word is a word, print it on screen.
    // Else if current Word is newline character, print space after this position.
    print_word_and_update_cursor();
&#125;

move_cursor_to(editor.cursor_x, editor.cursor_y);</code></pre></div><h3><b>2.4. 输入、输出函数联系</b></h3><div class="highlight"><pre><code class="language-text">while (1) &#123;
    refresh_screen();
    process_keypress();
&#125;</code></pre></div><h2><b>3. 想说的话~~(吐槽~~=。=</b></h2><p>从开始这个项目到现在很久很久了，最主要的问题是我很少找到可以借鉴的资料，导致战线超级长。这也从另一方面反映这东西的奇葩(=。=)</p><p>从一开始的想写一个自己的文本编辑器，到和编辑框杠上，有很多可以回忆的往事。所以虽然这东西简单，但我很想记录下来，它对我来说是非常重要的回忆。记得几次寒假一两周不出门，每天十几小时花在上面都是辛酸泪。</p><p>另外，我的Demo还有很多功能没有实现。比如：翻页、一些常用键功能……短期内不会再弄这东西了。</p><h2><b>4. 参考资料</b></h2><ol><li><a href="https://link.zhihu.com/?target=https%3A//github.com/Freder-chen/edit_box" class=" wrap external" target="_blank" rel="nofollow noreferrer">My demo in github</a></li><li><a href="https://link.zhihu.com/?target=http%3A//antirez.com/news/108" class=" wrap external" target="_blank" rel="nofollow noreferrer">Kilo</a></li><li><a href="https://link.zhihu.com/?target=https%3A//viewsourcecode.org/snaptoken/kilo/" class=" wrap external" target="_blank" rel="nofollow noreferrer">Kilo解析</a></li></ol>  
</div>
            