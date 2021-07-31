
---
title: '都 2021 了，你还忘记关闭 http body？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210729/8dae0146012cf0d6ef9ef38041de988a.jpg'
author: Dockone
comments: false
date: 2021-07-31 10:07:29
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210729/8dae0146012cf0d6ef9ef38041de988a.jpg'
---

<div>   
<br>看了看日历，现在已经是 2021 年了，偶尔还是能看到有人在发诸如 《http body 未关闭导致线上事故》，或者 《sql.Rows 未关闭半夜惊魂》类的文章，令人有一种梦回 2015 的感觉。<br>
<br>在这个 Go 的静态分析工具已经强到烂大街的时代，写这些文章除了暴露这些人所在的公司基础设施比较差，代码质量低以外，并不能体现出什么其它的意思了。毕竟哪怕是不懂怎么读源码，这样的问题你 Google 搜一下也知道是怎么回事了。<br>
<br>特别是有些人还挂着大公司的 title，让人更加不能理解了。下面是简单的静态分析工具的科普，希望给那些还在水深火热的 Gopher 们送点解药。<br>
<h3>何谓静态分析</h3>静态分析是通过扫描并解析用户代码，寻找代码中的潜在 bug 的一种手段。<br>
<br>静态分析一般会集成在项目上线的 CI 流程中，如果分析过程找到了 bug，会直接阻断上线，避免有问题的代码被部署到线上系统。从而在部署早期发现并修正潜在的问题。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210729/8dae0146012cf0d6ef9ef38041de988a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210729/8dae0146012cf0d6ef9ef38041de988a.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>社区常见 linter</h4>时至今日，社区已经有了丰富的 linter 资源供我们使用，本文会挑出一些常见 linter 进行说明。<br>
<br><strong>go lint</strong><br>
<br>go lint 是官方出的 linter，是 Go 语言最早期的 linter 了，其可以检查：<br>
<ul><li>导出函数是否有注释</li><li>变量、函数、包命名不符合 Go 规范，有下划线</li><li>receiver 命名是否不符合规范</li></ul><br>
<br>但这几年社区的 linter 蓬勃发展，所以这个项目也被官方 deprecated 掉了。其主要功能被另外一个 linter：<a href="https://revive.run/">revive</a> 完全继承了。<br>
<br><strong>go vet</strong><br>
<br>go vet 也是官方提供的静态分析工具，其内置了锁拷贝检查、循环变量捕获问题、printf 参数不匹配等工具。<br>
<br>比如新手老手都很容易犯的 loop capture 错误：<br>
<pre class="prettyprint">package main<br>
<br>
func main() &#123;<br>
var a = map[int]int &#123;1 : 1, 2: 3&#125;<br>
var b = map[int]*int&#123;&#125;<br>
for k, r := range a &#123;<br>
go func() &#123;<br>
b[k] = &r<br>
&#125;()<br>
&#125;<br>
&#125; <br>
</pre><br>
go vet 会直接把你骂醒：<br>
<pre class="prettyprint">~/test git:master ❯❯❯ go vet ./clo.go<br>
# command-line-arguments<br>
./clo.go:8:6: loop variable k captured by func literal<br>
./clo.go:8:12: loop variable r captured by func literal<br>
</pre><br>
执行 go tool vet help 可以看到 go vet 已经内置的一些 linter。<br>
<pre class="prettyprint">~ ❯❯❯ go tool vet help<br>
vet is a tool for static analysis of Go programs.<br>
<br>
vet examines Go source code and reports suspicious constructs,<br>
such as Printf calls whose arguments do not align with the format<br>
string. It uses heuristics that do not guarantee all reports are<br>
genuine problems, but it can find errors not caught by the compilers.<br>
<br>
Registered analyzers:<br>
<br>
asmdecl      report mismatches between assembly files and Go declarations<br>
assign       check for useless assignments<br>
atomic       check for common mistakes using the sync/atomic package<br>
bools        check for common mistakes involving boolean operators<br>
buildtag     check that +build tags are well-formed and correctly located<br>
cgocall      detect some violations of the cgo pointer passing rules<br>
composites   check for unkeyed composite literals<br>
copylocks    check for locks erroneously passed by value<br>
errorsas     report passing non-pointer or non-error values to errors.As<br>
httpresponse check for mistakes using HTTP responses<br>
loopclosure  check references to loop variables from within nested functions<br>
lostcancel   check cancel func returned by context.WithCancel is called<br>
nilfunc      check for useless comparisons between functions and nil<br>
printf       check consistency of Printf format strings and arguments<br>
shift        check for shifts that equal or exceed the width of the integer<br>
stdmethods   check signature of methods of well-known interfaces<br>
structtag    check that struct field tags conform to reflect.StructTag.Get<br>
tests        check for common mistaken usages of tests and examples<br>
unmarshal    report passing non-pointer or non-interface values to unmarshal<br>
unreachable  check for unreachable code<br>
unsafeptr    check for invalid conversions of uintptr to unsafe.Pointer<br>
unusedresult check for unused results of calls to some functions<br>
</pre><br>
默认情况下这些 linter 都是会跑的，当前很多 IDE 在代码修改时会自动执行 go vet，所以我们在写代码的时候一般就能发现这些错了。<br>
<br>但 <code class="prettyprint">go vet</code> 还是应该集成到线上流程中，因为有些程序员的下限实在太低。<br>
<br><strong>errcheck</strong><br>
<br>Go 语言中的大多数函数返回字段中都是有 error 的：<br>
<pre class="prettyprint">func sayhello(wr http.ResponseWriter, r *http.Request) &#123;<br>
io.WriteString(wr, "hello")<br>
&#125;<br>
<br>
func main() &#123;<br>
http.HandleFunc("/", sayhello)<br>
http.ListenAndServe(":1314", nil) // 这里返回的 err 没有处理<br>
&#125; <br>
</pre><br>
这个例子中，我们没有处理 <code class="prettyprint">http.ListenAndServe</code> 函数返回的 error 信息，这会导致我们的程序在启动时发生静默失败。<br>
<br>程序员往往会基于过往经验，对当前的场景产生过度自信，从而忽略掉一些常见函数的返回错误，这样的编程习惯经常为我们带来意外的线上事故。例如，规矩的写法是下面这样的：<br>
<pre class="prettyprint">data, err := getDataFromRPC()<br>
if err != nil &#123;<br>
return nil, err<br>
&#125;<br>
<br>
// do business logic<br>
age := data.age<br>
</pre><br>
而自信的程序员可能会写成这样：<br>
<pre class="prettyprint">data, _ := getDataFromRPC()<br>
<br>
// do business logic<br>
age := data.age<br>
</pre><br>
如果底层 RPC 逻辑出错，上层的 data 是个空指针也是很正常的，如果底层函数返回的 err 非空时，我们不应该对其它字段做任何的假设。这里 data 完全有可能是个空指针，造成用户程序 panic。<br>
<br>errcheck 会强制我们在代码中检查并处理 err。<br>
<br><strong>gocyclo</strong><br>
<br>gocyclo 主要用来检查函数的圈复杂度。圈复杂度可以参考下面的定义：<br>
<br><blockquote><br>圈复杂度（Cyclomatic complexity）是一种代码复杂度的衡量标准，在 1976 年由 Thomas J. McCabe, Sr. 提出。在软件测试的概念里，圈复杂度用来衡量一个模块判定结构的复杂程度，数量上表现为线性无关的路径条数，即合理的预防错误所需测试的最少路径条数。圈复杂度大说明程序代码可能质量低且难于测试和维护，根据经验，程序的可能错误和高的圈复杂度有着很大关系。</blockquote>看定义较为复杂但计算还是比较简单的，我们可以认为：<br>
<ul><li>一个 if，圈复杂度 + 1</li><li>一个 switch 的 case，圈复杂度 + 1</li><li>一个 for 循环，圈复杂度 + 1</li><li>一个 && 或 ||，圈复杂度 + 1</li></ul><br>
<br>在大多数语言中，若函数的圈复杂度超过了 10，那么我们就认为该函数较为复杂，需要做拆解或重构。部分场景可以使用表驱动的方式进行重构。<br>
<br>由于在 Go 语言中，我们使用 <code class="prettyprint">if err != nil</code> 来处理错误，所以在一个函数中出现多个 <code class="prettyprint">if err != nil</code> 是比较正常的，因此 Go 中函数复杂度的阈值可以稍微调高一些，15 是较为合适的值。<br>
<br>下面是在个人项目 elasticsql 中执行 gocyclo 的结果，输出 top 10 复杂的函数：<br>
<pre class="prettyprint">~/g/s/g/c/elasticsql git:master ❯❯❯ gocyclo -top 10  ./<br>
23 elasticsql handleSelectWhere select_handler.go:289:1<br>
16 elasticsql handleSelectWhereComparisonExpr select_handler.go:220:1<br>
16 elasticsql handleSelect select_handler.go:11:1<br>
9 elasticsql handleGroupByFuncExprDateHisto select_agg_handler.go:82:1<br>
9 elasticsql handleGroupByFuncExprDateRange select_agg_handler.go:154:1<br>
8 elasticsql buildComparisonExprRightStr select_handler.go:188:1<br>
7 elasticsql TestSupported select_test.go:80:1<br>
7 elasticsql Convert main.go:28:1<br>
7 elasticsql handleGroupByFuncExpr select_agg_handler.go:215:1<br>
6 elasticsql handleSelectWhereOrExpr select_handler.go:157:1<br>
</pre><br>
<strong>bodyclose</strong><br>
<br>使用 <a href="https://github.com/timakin/bodyclose">bodyclose</a> 可以帮我们检查在使用 HTTP 标准库时忘记关闭 http body 导致连接一直被占用的问题。<br>
<pre class="prettyprint">resp, err := http.Get("http://example.com/") // Wrong case<br>
if err != nil &#123;<br>
// handle error<br>
&#125;<br>
body, err := ioutil.ReadAll(resp.Body)<br>
</pre><br>
像上面这样的例子是不对的，使用标准库很容易犯这样的错。bodyclose 可以直接检查出这个问题：<br>
<pre class="prettyprint"># command-line-arguments<br>
./httpclient.go:10:23: response body must be closed<br>
</pre><br>
所以必须要把 Body 关闭：<br>
<pre class="prettyprint">resp, err := http.Get("http://example.com/")<br>
if err != nil &#123;<br>
// handle error<br>
&#125;<br>
defer resp.Body.Close() // OK<br>
body, err := ioutil.ReadAll(resp.Body)<br>
</pre><br>
HTTP 标准库的 API 设计的不太好，这个问题更好的避免方法是公司内部将 HTTP client 封装为 SDK，防止用户写出这样不 Close HTTP body 的代码。<br>
<br><strong>sqlrows</strong><br>
<br>与 HTTP 库设计类似，我们在面向数据库编程时，也会碰到 sql.Rows 忘记关闭的问题，导致连接大量被占用。<a href="https://github.com/gostaticanalysis/sqlrows">sqlrows</a> 这个 linter 能帮我们避免这个问题，先来看看错误的写法：<br>
<pre class="prettyprint">rows, err := db.QueryContext(ctx, "SELECT * FROM users")<br>
if err != nil &#123;<br>
return nil, err<br>
&#125;<br>
<br>
for rows.Next() &#123;<br>
err = rows.Scan(...)<br>
if err != nil &#123;<br>
return nil, err // NG: this return will not release a connection.<br>
&#125;<br>
&#125; <br>
</pre><br>
正确的写法需要在使用完后关闭 sql.Rows：<br>
<pre class="prettyprint">rows, err := db.QueryContext(ctx, "SELECT * FROM users")<br>
defer rows.Close() // NG: using rows before checking for errors<br>
if err != nil &#123;<br>
return nil, err<br>
&#125; <br>
</pre><br>
与 HTTP 同理，公司内也应该将 DB 查询封装为合理的 SDK，不要让业务使用标准库中的 API，避免上述错误发生。<br>
<br><strong>funlen</strong><br>
<br><a href="https://github.com/ultraware/funlen">funlen</a> 和 gocyclo 类似，但是这两个 linter 对代码复杂度的视角不太相同，gocyclo 更多关注函数中的逻辑分支，而 funlen 则重点关注函数的长度。默认函数超过 60 行和 40 条语句时，该 linter 即会报警。<br>
<h3>linter 集成工具</h3>一个一个去社区里找 linter 来拼搭效率太低，当前社区里已经有了较好的集成工具，早期是 gometalinter，后来性能更好，功能更全的 golangci-lint 逐渐取而代之。目前 golangci-lint 是 Go 社区的绝对主流 linter。<br>
<br><strong>golangci-lint</strong><br>
<br><a href="https://github.com/golangci/golangci-lint">golangci-lint</a> 能够通过配置来 enable 很多 linter，基本主流的都包含在内了。<br>
<br>在本节开头讲到的所有 linter 都可以在 golangci-lint 中进行配置，<br>
<br>使用也较为简单，只要在项目目录执行 golangci-lint run . 即可。<br>
<pre class="prettyprint">~/g/s/g/c/elasticsql git:master ❯❯❯ golangci-lint run .<br>
main.go:36:9: S1034: assigning the result of this type assertion to a variable (switch stmt := stmt.(type)) could eliminate type assertions in switch cases (gosimple)<br>
switch stmt.(type) &#123;<br>
    ^<br>
main.go:38:34: S1034(related information): could eliminate this type assertion (gosimple)<br>
dsl, table, err = handleSelect(stmt.(*sqlparser.Select))<br>
                             ^<br>
main.go:40:23: S1034(related information): could eliminate this type assertion (gosimple)<br>
return handleUpdate(stmt.(*sqlparser.Update))<br>
                  ^<br>
main.go:42:23: S1034(related information): could eliminate this type assertion (gosimple)<br>
return handleInsert(stmt.(*sqlparser.Insert))<br>
                  ^<br>
select_handler.go:192:9: S1034: assigning the result of this type assertion to a variable (switch expr := expr.(type)) could eliminate type assertions in switch cases (gosimple)<br>
switch expr.(type) &#123; <br>
</pre><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/CcnW7FvY1yzU4HI-QK7ymQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/CcnW7FvY1yzU4HI-QK7ymQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            