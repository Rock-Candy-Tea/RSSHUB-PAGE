
---
title: 'Linux进程之如何查看进程详情？'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/16753854-e0b1319fc01fe5f1.jpg'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/16753854-e0b1319fc01fe5f1.jpg'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="720"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-e0b1319fc01fe5f1.jpg" data-original-width="1080" data-original-height="720" data-original-format="image/jpeg" data-original-filesize="57081" src="https://upload-images.jianshu.io/upload_images/16753854-e0b1319fc01fe5f1.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h1>1. ps是什么？</h1>
<p>要对进程进行监测和控制，首先必须要了解当前进程的情况,也就是需要查看当前进程，ps命令就是最基本进程查看命令。使用该命令可以确定有哪些进程正在运行和运行的状态、进程是否结束、进程有没有僵尸、哪些进程占用了过多的资源等等.总之大部分信息都是可以通过执行该命令得到。</p>
<p><strong>ps是显示瞬间进程的状态，并不动态连续</strong>；如果想对进程进行实时监控应该用top命令。</p>
<p><strong>基本参数：</strong></p>
<ul>
<li>-A ：所有的进程均显示出来，与 -e 具有同样的效用；</li>
<li>-a ： 显示现行终端机下的所有进程，包括其他用户的进程；</li>
<li>-u ：以用户为主的进程状态 ；</li>
<li>x ：通常与 a 这个参数一起使用，可列出较完整信息。</li>
</ul>
<p><strong>输出格式规划：</strong></p>
<ul>
<li>l ：较长、较详细的将该PID 的的信息列出；</li>
<li>j ：工作的格式 (jobs format)</li>
<li>-f ：做一个更为完整的输出。</li>
</ul>
<p>下面我们就来一个命令进行实践，看看不同的参数都有些什么效果。</p>
<hr>
<h1>2. 不加参数执行ps命令会输出什么？</h1>
<p>这是一个基本的 <strong>ps</strong> 使用，我们来看看控制台中执行这个命令并查看结果。<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="648" data-height="117"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-2b030a207cd25197.png" data-original-width="648" data-original-height="117" data-original-format="image/png" data-original-filesize="31162" src="https://upload-images.jianshu.io/upload_images/16753854-2b030a207cd25197.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><br>
结果默认会显示4列信息：<p></p>
<ul>
<li>PID: 运行着的命令(CMD)的进程编号</li>
<li>TTY: 命令所运行的位置（终端）</li>
<li>TIME: 运行着的该命令所占用的CPU处理时间</li>
<li>CMD: 该进程所运行的命令</li>
</ul>
<p>这些信息在显示时未排序。</p>
<hr>
<h1>3. 如何显示所有当前进程？</h1>
<p>使用 <strong>-a</strong> 参数，<strong>-a 代表 all</strong>。同时加上x参数会显示没有控制终端的进程。</p>
<pre><code>$ ps -ax

</code></pre>
<p>这个命令的结果或许会很长。为了便于查看，可以结合less命令和管道来使用。</p>
<pre><code>$ ps -ax | less

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="652" data-height="346"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-89f2746651e7428e.png" data-original-width="652" data-original-height="346" data-original-format="image/png" data-original-filesize="99287" src="https://upload-images.jianshu.io/upload_images/16753854-89f2746651e7428e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h1>4. 如何根据进程的用户进行信息过滤呢？</h1>
<p>在需要查看特定用户进程的情况下，我们可以使用 <strong>-u</strong> 参数。比如我们要查看用户'pungki'的进程，可以通过下面的命令：</p>
<pre><code>$ ps -u pungki

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="350" data-height="206"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-fe789ba7e4cf45ce.png" data-original-width="350" data-original-height="206" data-original-format="image/png" data-original-filesize="17386" src="https://upload-images.jianshu.io/upload_images/16753854-fe789ba7e4cf45ce.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h1>5. 如何通过cpu和内存使用来过滤进程？</h1>
<p>也许你希望把结果按照 CPU 或者内存用量来筛选，这样你就找到哪个进程占用了你的资源。要做到这一点，我们可以使用 <strong>aux</strong> 参数，来显示全面的信息:</p>
<pre><code>$ ps -aux | less

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="652" data-height="337"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-a18840ff7d03d313.png" data-original-width="652" data-original-height="337" data-original-format="image/png" data-original-filesize="173723" src="https://upload-images.jianshu.io/upload_images/16753854-a18840ff7d03d313.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>当结果很长时，我们可以使用管道和less命令来筛选。</p>
<p>默认的结果集是未排好序的。可以通过 <strong>--sort</strong>命令来排序。</p>
<h3>5.1 根据CPU使用率来升序排序</h3>
<pre><code>$ ps -aux --sort -pcpu | less

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="654" data-height="218"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-f3ced63c60e903c4.png" data-original-width="654" data-original-height="218" data-original-format="image/png" data-original-filesize="147973" src="https://upload-images.jianshu.io/upload_images/16753854-f3ced63c60e903c4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>5.2 根据内存使用率来升序排序</h3>
<pre><code>$ ps -aux --sort -pmem | less

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="657" data-height="260"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-1db58e5b9b487311.png" data-original-width="657" data-original-height="260" data-original-format="image/png" data-original-filesize="206482" src="https://upload-images.jianshu.io/upload_images/16753854-1db58e5b9b487311.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>5.3 我们也可以将它们合并到一个命令，并通过管道显示前10个结果：</h3>
<pre><code>$ ps -aux --sort -pcpu,+pmem | head -n 10

</code></pre>
<hr>
<h1>6. 如何通过进程名和PID进行过滤呢？</h1>
<p>使用 <strong>-C</strong> 参数，后面跟你要找的进程的名字。比如想显示一个名为getty的进程的信息，就可以使用下面的命令：</p>
<pre><code>$ ps -C getty
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="397" data-height="169"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-b9eadb134d2d6550.png" data-original-width="397" data-original-height="169" data-original-format="image/png" data-original-filesize="11831" src="https://upload-images.jianshu.io/upload_images/16753854-b9eadb134d2d6550.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>如果想要看到更多的细节，我们可以使用-f参数来查看格式化的信息列表：</p>
<pre><code>$ ps -f -C getty

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="620" data-height="165"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-70519c4761ade3df.png" data-original-width="620" data-original-height="165" data-original-format="image/png" data-original-filesize="27756" src="https://upload-images.jianshu.io/upload_images/16753854-70519c4761ade3df.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h1>7. 如何根据线程来过滤进程呢？</h1>
<p>如果我们想知道特定进程的线程，可以使用 <strong>-L</strong> 参数，后面加上特定的PID。</p>
<pre><code>$ ps -L 1213

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="472" data-height="175"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-7d55a7e12d7f416a.png" data-original-width="472" data-original-height="175" data-original-format="image/png" data-original-filesize="12086" src="https://upload-images.jianshu.io/upload_images/16753854-7d55a7e12d7f416a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h1>8. 如何树形的显示进程？</h1>
<p>有时候我们希望以树形结构显示进程，可以使用 <strong>-axjf</strong> 参数。</p>
<pre><code>$ ps -axjf

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="654" data-height="152"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-18c0747511fa83e1.png" data-original-width="654" data-original-height="152" data-original-format="image/png" data-original-filesize="86096" src="https://upload-images.jianshu.io/upload_images/16753854-18c0747511fa83e1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>或者可以使用另一个命令。</p>
<pre><code>$ pstree

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="476" data-height="342"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-768d2b3d85f63a56.png" data-original-width="476" data-original-height="342" data-original-format="image/png" data-original-filesize="32088" src="https://upload-images.jianshu.io/upload_images/16753854-768d2b3d85f63a56.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h1>9. 如何显示安全信息？</h1>
<p>如果想要查看现在有谁登入了你的服务器。可以使用ps命令加上相关参数:</p>
<pre><code>$ ps -eo pid,user,args

</code></pre>
<p>参数 <strong>-e</strong> 显示所有进程信息，<strong>-o</strong> 参数控制输出。<strong>Pid</strong>,<strong>User</strong> 和 <strong>Args</strong>参数显示PID，<strong>运行应用的用户</strong>和<strong>该应用</strong>。<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="553" data-height="160"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-571bba5bec3b3bc1.png" data-original-width="553" data-original-height="160" data-original-format="image/png" data-original-filesize="29184" src="https://upload-images.jianshu.io/upload_images/16753854-571bba5bec3b3bc1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><p></p>
<p>能够与 <strong>-e</strong> 参数 一起使用的关键字是<strong>args, cmd, comm, command, fname, ucmd, ucomm, lstart, bsdstart 和 start</strong>。</p>
<hr>
<h1>10. 如何格式化输出root用户（真实的或有效的UID）创建的进程？</h1>
<p>系统管理员想要查看由root用户运行的进程和这个进程的其他相关信息时，可以通过下面的命令:</p>
<pre><code>$ ps -U root -u root u

</code></pre>
<p><strong>-U</strong> 参数按真实用户ID(RUID)筛选进程，它会从用户列表中选择真实用户名或 ID。真实用户即实际创建该进程的用户。</p>
<p><strong>-u</strong> 参数用来筛选有效用户ID（EUID）。</p>
<p>最后的 <strong>u</strong> 参数用来决定以针对用户的格式输出，由<strong>User, PID, %CPU, %MEM, VSZ, RSS, TTY, STAT, START, TIME 和 COMMAND</strong>这几列组成。</p>
<p>这里有上面的命令的输出结果：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="638" data-height="341"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-ad374c3caa071b93.png" data-original-width="638" data-original-height="341" data-original-format="image/png" data-original-filesize="58167" src="https://upload-images.jianshu.io/upload_images/16753854-ad374c3caa071b93.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h1>11. 如何使用PS实时监控进程状态？</h1>
<p>ps 命令会显示你系统当前的进程状态，但是这个结果是静态的。</p>
<p>当有一种情况，我们需要像上面第四点中提到的通过CPU和内存的使用率来筛选进程，并且我们希望结果能够每秒刷新一次。为此，我们可以<strong>将ps命令和watch命令结合起来</strong>。</p>
<pre><code>$ watch -n 1 ‘ps -aux --sort -pmem, -pcpu’

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="649" data-height="503"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-926627695a6cbe8b.png" data-original-width="649" data-original-height="503" data-original-format="image/png" data-original-filesize="372038" src="https://upload-images.jianshu.io/upload_images/16753854-926627695a6cbe8b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>如果输出太长，我们也可以限制它，比如前20条，我们可以使用 <strong>head</strong> 命令来做到。</p>
<pre><code>$ watch -n 1 ‘ps -aux --sort -pmem, -pcpu | head 20’

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="651" data-height="409"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-d5efdf3a1590d985.png" data-original-width="651" data-original-height="409" data-original-format="image/png" data-original-filesize="256715" src="https://upload-images.jianshu.io/upload_images/16753854-d5efdf3a1590d985.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>这里的动态查看并不像top或者htop命令一样。但是使用ps的好处是你能够定义显示的字段，你能够选择你想查看的字段。</p>
<p>举个例子，如果你只需要看名为'pungki'用户的信息，你可以使用下面的命令：</p>
<pre><code>$ watch -n 1 ‘ps -aux -U pungki u --sort -pmem, -pcpu | head 20’

</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="654" data-height="388"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-1069cb12da4fc8ef.png" data-original-width="654" data-original-height="388" data-original-format="image/png" data-original-filesize="83948" src="https://upload-images.jianshu.io/upload_images/16753854-1069cb12da4fc8ef.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h1>12. 最后</h1>
<p>你也许每天都会使用ps命令来监控你的Linux系统。但是事实上，你可以通过ps命令的参数来生成各种你需要的报表。</p>
<p>ps命令的另一个优势是ps是各种 Linux系统都默认安装的，因此你只要用就行了。不要忘了通过 man ps来查看更多的参数。</p>
<blockquote>
<p>文章来源：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fjuejin.im%2Fpost%2F5bf9213ce51d452237153c5c" target="_blank">https://juejin.im/post/5bf9213ce51d452237153c5c</a></p>
</blockquote>
<hr>
  
</div>
            