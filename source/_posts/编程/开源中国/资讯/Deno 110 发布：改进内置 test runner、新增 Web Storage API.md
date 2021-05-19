
---
title: 'Deno 1.10 发布：改进内置 test runner、新增 Web Storage API'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1795'
author: 开源中国
comments: false
date: Wed, 19 May 2021 07:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1795'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:start"> 
 <div style="text-align:justify"> 
  <p style="text-align: start;"><span style="background-color:#ffffff"><span style="color:#333333">Deno 1.10 已正式发布，此版本包含许多新功能、性能优化以及错误修复。</span></span></p> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.10%23improvements-to-deno-test" target="_blank">改进内置的 test runner</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.10%23worker.postmessage-supports-structured-clone-algorithm" target="_blank">在 Web Workers 中支持结构化克隆 (structured clone)</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.10%23support-for-web-storage-api" target="_blank">新增 Web Storage API</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.10%23support-remote-import-maps" target="_blank">支持远程导入映射 (maps)</a></li> 
  </ul> 
 </div> 
</div> 
<p><span style="background-color:#ffffff"><span style="color:#333333"><span style="color:#333333">如果已经安装了 Deno，运行</span></span></span><code>deno upgrade</code><span style="background-color:#ffffff"><span style="color:#333333"><span style="color:#333333">命令即可升级到 1.10 版本。如果是首次安装，可以参考下面的方法：</span></span></span></p> 
<pre><code class="language-bash"># Using Shell (macOS and Linux):
curl -fsSL https://deno.land/x/install/install.sh | sh

# Using PowerShell (Windows):
iwr https://deno.land/x/install/install.ps1 -useb | iex

# Using Homebrew (macOS):
brew install deno

# Using Scoop (Windows):
scoop install deno

# Using Chocolatey (Windows):
choco install deno</code></pre> 
<h1>改进内置的 test runner</h1> 
<p>Deno 1.10 对内置的 test runner 进行了重大改进。</p> 
<ul> 
 <li>支持隔离和并行执行测试</li> 
 <li>支持为测试用例指定可配置的确切权限</li> 
</ul> 
<pre><code class="language-javascript">Deno.test(&#123;
  name: "write only",
  permissions: &#123; write: true, read: false &#125;,
  async fn() &#123;
    await Deno.writeTextFile("./foo.txt", "I can write!");
    console.log(await Deno.readTextFile("./foo.txt"));
  &#125;,
&#125;);</code></pre> 
<pre><code class="language-javascript">$ deno test --allow-read --allow-write --unstable test_permissions.ts
Check file:///Users/ry/src/deno/test_permissions.ts
running 1 test from file:///Users/ry/src/deno/test_permissions.ts
test write only ... FAILED (5ms)

failures:

write only
PermissionDenied: Requires read access to "./foo.txt", run again with the --allow-read flag
    at deno:core/core.js:86:46
    at unwrapOpResult (deno:core/core.js:106:13)
    at async open (deno:runtime/js/40_files.js:46:17)
    at async Object.readTextFile (deno:runtime/js/40_read_file.js:40:18)
    at async fn (file:///Users/ry/src/deno/test_permissions.ts:6:17)
    at async asyncOpSanitizer (deno:runtime/js/40_testing.js:21:9)
    at async resourceSanitizer (deno:runtime/js/40_testing.js:58:7)
    at async exitSanitizer (deno:runtime/js/40_testing.js:85:9)
    at async runTest (deno:runtime/js/40_testing.js:199:7)
    at async Object.runTests (deno:runtime/js/40_testing.js:244:7)

failures:

write only

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out (37ms)</code></pre> 
<ul> 
 <li>更好地展示 test runner 输出内容</li> 
</ul> 
<pre><code>running 4 tests from file:///dev/deno/cli/tests/unit/tty_test.ts
test consoleSizeFile ... ok (11ms)
test consoleSizeError ... ok (4ms)
test isatty ... ok (4ms)
test isattyError ... ok (3ms)
running 6 tests from file:///dev/deno/cli/tests/unit/rename_test.ts
test renameSyncSuccess ... ok (17ms)
test renameSyncReadPerm ... ok (5ms)
test renameSyncWritePerm ... ok (6ms)
test renameSuccess ... ok (13ms)
test renameSyncErrorsUnix ... ok (34ms)
test renameSyncErrorsWin ... ignored (1ms)
...</code></pre> 
<ul> 
 <li>支持运行测试时监视文件更改</li> 
 <li>支持在文档中进行类型检测</li> 
</ul> 
<pre><code class="language-javascript">/**
 * ```
 * import &#123; example &#125; from "./test_docs.ts";
 *
 * console.assert(example() == 42);
 * ```
 */
export function example(): string &#123;
  return "example";
&#125;</code></pre> 
<p>示例如下：</p> 
<pre><code>$ deno test --doc https://deno.com/v1.10/test_docs.ts

Check file:///dev/test_docs.ts:2-7
error: TS2367 [ERROR]: This condition will always return 'false' since the types 'string' and 'number' have no overlap.
console.assert(example() == 42);
               ~~~~~~~~~~~~~~~
    at file:///dev/test_docs.ts:2-7.ts:3:16</code></pre> 
<h1>新增 Web Storage API</h1> 
<p style="text-align:start"><span style="color:#24292e">此版本增加了对 Web Storage API 的支持。该 API 由<code>localStorage</code>和<code>sessionStorage</code>组成，可以用于持久存储少量数据，而无需直接访问文件系统。开发者可以不需要申请任何权限来使用<code>localStorage</code>和<code>sessionStorage</code>。</span></p> 
<p style="text-align:start"><span style="color:#24292e">底层存储层和持久性对于应用程序是不透明的，因此不用担心安全性的问题。</span></p> 
<p style="text-align:start"><span style="color:#24292e">该 API 的工作方式与在浏览器中一样：<code>localStorage</code>可用于在流程重新启动时永久存储多达 5MB 的数据，而 <code>sessionStorage</code>可用于在流程持续时间内存储少量数据。</span></p> 
<p style="text-align:start"><span style="color:#24292e">下面是一个简单的例子：</span></p> 
<pre><code class="language-javascript">// kv.ts

const key = Deno.args[0];

if (key === undefined) &#123;
  // if user passes no args, display number of entries
  console.log(localStorage.length);
&#125; else &#123;
  const value = Deno.args[1];

  if (value === undefined) &#123;
    // if no value is specified, return value of the key
    console.log(localStorage.getItem(key));
  &#125; else &#123;
    // if value is specifed, set the value
    localStorage.setItem(key, value);
  &#125;
&#125;</code></pre> 
<pre><code>$ deno run --location https://example.com ./kv.ts
0
$ deno run --location https://example.com ./kv.ts foo bar
$ deno run --location https://example.com ./kv.ts foo
bar
$ deno run --location https://example.com ./kv.ts
1</code></pre> 
<h1>支持远程导入映射 (maps)</h1> 
<p>Deno 1.8 中导入映射功能已稳定，到了 Deno 1.10，目前已启用远程导入映射功能。这意味着导入映射现在不必存储在本地文件系统上，它们也可以通过 HTTP 进行加载：</p> 
<pre><code>$ deno install --import-map=https://example.com/import_map.json -n example https://example.com/mod.ts</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.10" target="_blank">详细内容查看发布公告</a><span style="background-color:#ffffff"><span style="color:#333333">。</span></span></p>
                                        </div>
                                      
</div>
            