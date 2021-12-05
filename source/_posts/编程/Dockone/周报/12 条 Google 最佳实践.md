
---
title: '12 条 Google 最佳实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211205/e1bcb1019b1383db2bbfb502d52c76f7.png'
author: Dockone
comments: false
date: 2021-12-05 13:15:06
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211205/e1bcb1019b1383db2bbfb502d52c76f7.png'
---

<div>   
<br>这是直接总结好的 12 条，详细的再继续往下看：<br>
<ol><li>先处理错误避免嵌套</li><li>尽量避免重复</li><li>先写最重要的代码</li><li>给代码写文档注释</li><li>命名尽可能简洁</li><li>使用多文件包</li><li>使用  <code class="prettyprint">go get</code>  可获取你的包</li><li>了解自己的需求</li><li>保持包的独立性</li><li>避免在内部使用并发</li><li>使用 Goroutine 管理状态</li><li>避免 Goroutine 泄露</li></ol><br>
<br><h3>最佳实践</h3>这是一篇翻译文章，为了使读者更好的理解，会在原文翻译的基础增加一些讲解或描述。<br>
<br>来在维基百科：<br>
<br><blockquote><br>A best practice is a method or technique that has consistently shown results superior to those achieved with other means<br>
  最佳实践是一种方法或技术，其结果始终优于其他方式。</blockquote>写 Go 代码时的技术要求：<br>
<ul><li>简单性</li><li>可读性</li><li>可维护性</li></ul><br>
<br><h3>样例代码</h3>需要优化的代码。<br>
<pre class="prettyprint">type Gopher struct &#123;<br>
Name     string<br>
AgeYears int<br>
&#125;<br>
<br>
func (g *Gopher) WriteTo(w io.Writer) (size int64, err error) &#123;<br>
err = binary.Write(w, binary.LittleEndian, int32(len(g.Name)))<br>
if err == nil &#123;<br>
    size += 4<br>
    var n int<br>
    n, err = w.Write([]byte(g.Name))<br>
    size += int64(n)<br>
    if err == nil &#123;<br>
        err = binary.Write(w, binary.LittleEndian, int64(g.AgeYears))<br>
        if err == nil &#123;<br>
            size += 4<br>
        &#125;<br>
        return<br>
    &#125;<br>
    return<br>
&#125;<br>
return<br>
&#125; <br>
</pre><br>
看看上面的代码，自己先思索在代码编写方式上怎么更好，我先简单说下代码意思是啥：<br>
<ul><li>将  <code class="prettyprint">Name</code>  和  <code class="prettyprint">AgeYears</code>  字段数据存入  <code class="prettyprint">io.Writer</code>  类型中。</li><li>如果存入的数据是  <code class="prettyprint">string</code>  或  <code class="prettyprint">[]byte</code>  类型，再追加其长度数据。</li></ul><br>
<br>如果对  <code class="prettyprint">binary</code>  这个标准包不知道怎么使用，就看看我的另一篇文章<a href="https://mp.weixin.qq.com/s/fATns17paqbmG8Ikb3ZedA">《快速了解 “小字端” 和 “大字端” 及 Go 语言中的使用》</a>  。<br>
<h3>先处理错误避免嵌套</h3><pre class="prettyprint">func (g *Gopher) WriteTo(w io.Writer) (size int64, err error) &#123;<br>
err = binary.Write(w, binary.LittleEndian, int32(len(g.Name)))<br>
if err != nil &#123;<br>
    return<br>
&#125;<br>
size += 4<br>
n, err := w.Write([]byte(g.Name))<br>
size += int64(n)<br>
if err != nil &#123;<br>
    return<br>
&#125;<br>
err = binary.Write(w, binary.LittleEndian, int64(g.AgeYears))<br>
if err == nil &#123;<br>
    size += 4<br>
&#125;<br>
return<br>
&#125; <br>
</pre><br>
减少判断错误的嵌套，会使读者看起来更轻松。<br>
<h3>尽量避免重复</h3>上面代码中  <code class="prettyprint">WriteTo</code>  方法中的  <code class="prettyprint">Write</code>  出现了 3 次，比较重复，精简后如下：<br>
<pre class="prettyprint">type binWriter struct &#123;<br>
w    io.Writer<br>
size int64<br>
err  error<br>
&#125;<br>
<br>
// Write writes a value to the provided writer in little endian form. func (w *binWriter) Write(v interface&#123;&#125;) &#123;<br>
if w.err != nil &#123;<br>
    return<br>
&#125;<br>
if w.err = binary.Write(w.w, binary.LittleEndian, v); w.err == nil &#123;<br>
    w.size += int64(binary.Size(v))<br>
&#125;<br>
&#125; <br>
</pre><br>
使用  <code class="prettyprint">binWriter</code>  结构体。<br>
<pre class="prettyprint">func (g *Gopher) WriteTo(w io.Writer) (int64, error) &#123;<br>
bw := &binWriter&#123;w: w&#125;<br>
bw.Write(int32(len(g.Name)))<br>
bw.Write([]byte(g.Name))<br>
bw.Write(int64(g.AgeYears))<br>
return bw.size, bw.err<br>
&#125; <br>
</pre><br>
<h3>type-switch 处理不同类型</h3><pre class="prettyprint">func (w *binWriter) Write(v interface&#123;&#125;) &#123;<br>
if w.err != nil &#123;<br>
    return<br>
&#125;<br>
switch v.(type) &#123;<br>
case string:<br>
    s := v.(string)<br>
    w.Write(int32(len(s)))<br>
    w.Write([]byte(s))<br>
case int:<br>
    i := v.(int)<br>
    w.Write(int64(i))<br>
default:<br>
    if w.err = binary.Write(w.w, binary.LittleEndian, v); w.err == nil &#123;<br>
        w.size += int64(binary.Size(v))<br>
    &#125;<br>
&#125;<br>
&#125;<br>
<br>
func (g *Gopher) WriteTo(w io.Writer) (int64, error) &#123;<br>
bw := &binWriter&#123;w: w&#125;<br>
bw.Write(g.Name)<br>
bw.Write(g.AgeYears)<br>
return bw.size, bw.err<br>
&#125; <br>
</pre><br>
<h3>type-switch 精简</h3>摒弃了上面代码的  <code class="prettyprint">v.(string)</code>  、<code class="prettyprint">v.(int)</code>  类型反射使用。<br>
<pre class="prettyprint">func (w *binWriter) Write(v interface&#123;&#125;) &#123;<br>
if w.err != nil &#123;<br>
    return<br>
&#125;<br>
switch x := v.(type) &#123;<br>
case string:<br>
    w.Write(int32(len(x)))<br>
    w.Write([]byte(x))<br>
case int:<br>
    w.Write(int64(x))<br>
default:<br>
    if w.err = binary.Write(w.w, binary.LittleEndian, v); w.err == nil &#123;<br>
        w.size += int64(binary.Size(v))<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
进入不同分支，<code class="prettyprint">x</code>  变量对应的就是该分支的类型。<br>
<h3>自行决定是否写入</h3><pre class="prettyprint">type binWriter struct &#123;<br>
w   io.Writer<br>
buf bytes.Buffer<br>
err error<br>
&#125;<br>
<br>
// Write writes a value to the provided writer in little endian form. func (w *binWriter) Write(v interface&#123;&#125;) &#123;<br>
if w.err != nil &#123;<br>
    return<br>
&#125;<br>
switch x := v.(type) &#123;<br>
case string:<br>
    w.Write(int32(len(x)))<br>
    w.Write([]byte(x))<br>
case int:<br>
    w.Write(int64(x))<br>
default:<br>
    w.err = binary.Write(&w.buf, binary.LittleEndian, v)<br>
&#125;<br>
&#125;<br>
<br>
// Flush writes any pending values into the writer if no error has occurred. // If an error has occurred, earlier or with a write by Flush, the error is // returned. func (w *binWriter) Flush() (int64, error) &#123;<br>
if w.err != nil &#123;<br>
    return 0, w.err<br>
&#125;<br>
return w.buf.WriteTo(w.w)<br>
&#125;<br>
<br>
func (g *Gopher) WriteTo(w io.Writer) (int64, error) &#123;<br>
bw := &binWriter&#123;w: w&#125;<br>
bw.Write(g.Name)<br>
bw.Write(g.AgeYears)<br>
return bw.Flush()<br>
&#125; <br>
</pre><br>
<code class="prettyprint">WriteTo</code>  方法中，分了两大部分，增加了灵活性：<br>
<ul><li>组装信息</li><li>调用  <code class="prettyprint">Flush</code>  方法来决定是否写入  <code class="prettyprint">w</code>。</li></ul><br>
<br><h3>函数适配器</h3><pre class="prettyprint">func init() &#123;<br>
http.HandleFunc("/", handler)<br>
&#125;<br>
<br>
func handler(w http.ResponseWriter, r *http.Request) &#123;<br>
err := doThis()<br>
if err != nil &#123;<br>
    http.Error(w, err.Error(), http.StatusInternalServerError)<br>
    log.Printf("handling %q: %v", r.RequestURI, err)<br>
    return<br>
&#125;<br>
<br>
err = doThat()<br>
if err != nil &#123;<br>
    http.Error(w, err.Error(), http.StatusInternalServerError)<br>
    log.Printf("handling %q: %v", r.RequestURI, err)<br>
    return<br>
&#125;<br>
&#125; <br>
</pre><br>
函数  <code class="prettyprint">handler</code>  包含了业务的逻辑和错误处理，下来将错误处理单独写一个函数处理，代码修改如下：<br>
<pre class="prettyprint">func init() &#123;<br>
http.HandleFunc("/", errorHandler(betterHandler))<br>
&#125;<br>
<br>
func errorHandler(f func(http.ResponseWriter, *http.Request) error) http.HandlerFunc &#123;<br>
return func(w http.ResponseWriter, r *http.Request) &#123;<br>
    err := f(w, r)<br>
    if err != nil &#123;<br>
        http.Error(w, err.Error(), http.StatusInternalServerError)<br>
        log.Printf("handling %q: %v", r.RequestURI, err)<br>
    &#125;<br>
&#125;<br>
&#125;<br>
<br>
func betterHandler(w http.ResponseWriter, r *http.Request) error &#123;<br>
if err := doThis(); err != nil &#123;<br>
    return fmt.Errorf("doing this: %v", err)<br>
&#125;<br>
<br>
if err := doThat(); err != nil &#123;<br>
    return fmt.Errorf("doing that: %v", err)<br>
&#125;<br>
return nil<br>
&#125; <br>
</pre><br>
<h3>组织你的代码</h3><h4>先写最重要的</h4>许可信息、构建信息、包文档。<br>
<br><code class="prettyprint">import</code>  语句：相关联组使用空行分隔。<br>
<pre class="prettyprint">import (<br>
"fmt"<br>
"io"<br>
"log"<br>
<br>
"golang.org/x/net/websocket"<br>
) <br>
</pre><br>
其余代码，以最重要的类型开始，以辅助函数和类型结尾。<br>
<h4>文档注释</h4>包名前的相关文档。<br>
<pre class="prettyprint">// Package playground registers an HTTP handler at "/compile" that // proxies requests to the golang.org playground service. package playground<br>
</pre><br>
Go 语言中的标示符（变量、结构体等等）在 godoc 导出的文章中应该被正确的记录下来。<br>
<pre class="prettyprint">// Author represents the person who wrote and/or is presenting the document. type Author struct &#123;<br>
Elem []Elem<br>
&#125;<br>
<br>
// TextElem returns the first text elements of the author details. // This is used to display the author' name, job title, and company // without the contact details. func (p *Author) TextElem() (elems []Elem) &#123; <br>
</pre><br>
扩展：<br>
<br>使用 godoc 工具在网页上查看 go 项目文档。<br>
<pre class="prettyprint"># 安装<br>
go get golang.org/x/tools/cmd/godoc<br>
<br>
# 启动服务<br>
godoc -http=:6060<br>
</pre><br>
直接在本地访问  <a href="http://localhost:6060/">localhost:6060</a>  查看文档。<br>
<h4>命名尽可能简洁</h4>或者说，长命名不一定好。<br>
<br>尽可能找到一个可以清晰表达的简短命名，例如：<br>
<ul><li><code class="prettyprint">MarshalIndent</code>  比  <code class="prettyprint">MarshalWithIndentation</code>  好。</li></ul><br>
<br>不要忘了，在调用包内容时，会先写包名。<br>
<ul><li>在  <code class="prettyprint">encoding/json</code>  包内，有一个结构体  <code class="prettyprint">Encoder</code>，不要写成  <code class="prettyprint">JSONEncoder</code>。</li><li>这样被使用  <code class="prettyprint">json.Encoder</code>  。</li></ul><br>
<br><h4>多文件包</h4>是否应该将一个包拆分到多个文件？<br>
<ul><li>应避免代码太长</li></ul><br>
<br>标准包  <code class="prettyprint">net/http</code>  总共 15734 行代码，被拆分到 47 个文件中。<br>
<ul><li>拆分代码和测试。</li></ul><br>
<br>net/http/cookie.go 和 net/http/cookie_test.go 文件都放置在 http 包下。<br>
<br>测试代码<strong>只有</strong>在测试时才被编译。<br>
<ul><li>拆分包文档</li></ul><br>
<br>当在一个包内有多个文件时，按照惯例，创建一个 doc.go 文件编写包的文档描述。<br>
<br><strong>个人思考</strong>：当一个包的说明信息比较多时，可以考虑创建 doc.go 文件。<br>
<h4>使用 go get 可获取你的包</h4>当你的包被提供使用时，应该清晰的让使用者知道哪些可复用，哪些不可复用。<br>
<br>所以，当一些包可能会被复用，有些则不会的情况下怎么做？<br>
<br>例如：定义一些网络协议的包可能会复用，而定义一些可执行命令的包则不会。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211205/e1bcb1019b1383db2bbfb502d52c76f7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211205/e1bcb1019b1383db2bbfb502d52c76f7.png" class="img-polaroid" title="2-1.png" alt="2-1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><code class="prettyprint">cmd</code>  可执行命令的包，不提供复用</li><li><code class="prettyprint">pkg</code>  可复用的包</li></ul><br>
<br><strong>个人思考</strong>：如果一个项目中的可执行入口比较多，建议放置在 cmd 目录中，而对于 pkg 目录目前是不太建议，所以不用借鉴。<br>
<h3>API</h3><h4>了解自己的需求</h4>我们继续使用之前的 Gopher 类型。<br>
<pre class="prettyprint">type Gopher struct &#123;<br>
Name     string<br>
AgeYears int<br>
&#125; <br>
</pre><br>
我们可以定义这个方法。<br>
<pre class="prettyprint">func (g *Gopher) WriteToFile(f *os.File) (int64, error) &#123; <br>
</pre><br>
但方法的参数使用具体的类型时会变得难以测试，因此我们使用接口。<br>
<pre class="prettyprint">func (g *Gopher) WriteToReadWriter(rw io.ReadWriter) (int64, error) &#123; <br>
</pre><br>
并且，当使用了接口后，我们应该只需定义我们所需要的方法。<br>
<pre class="prettyprint">func (g *Gopher) WriteToWriter(f io.Writer) (int64, error) &#123; <br>
</pre><br>
<h4>保持包的独立性</h4><pre class="prettyprint">import (<br>
"golang.org/x/talks/content/2013/bestpractices/funcdraw/drawer"<br>
"golang.org/x/talks/content/2013/bestpractices/funcdraw/parser"<br>
)` <br>
<br>
`// Parse the text into an executable function.   f, err := parser.Parse(text)<br>
if err != nil &#123;<br>
  log.Fatalf("parse %q: %v", text, err)<br>
&#125;<br>
<br>
// Create an image plotting the function.   m := drawer.Draw(f, *width, *height, *xmin, *xmax)<br>
<br>
// Encode the image into the standard output.   err = png.Encode(os.Stdout, m)<br>
if err != nil &#123;<br>
  log.Fatalf("encode image: %v", err)<br>
&#125; <br>
</pre><br>
代码中  <code class="prettyprint">Draw</code>  方法接受了  <code class="prettyprint">Parse</code>  函数返回的  <code class="prettyprint">f</code>  变量，从逻辑上看  <code class="prettyprint">drawer</code>  包依赖  <code class="prettyprint">parser</code>  包，下来看看如何取消这种依赖性。<br>
<br><code class="prettyprint">parser</code>  包：<br>
<pre class="prettyprint">type ParsedFunc struct &#123;<br>
text string<br>
eval func(float64) float64<br>
&#125;<br>
<br>
func Parse(text string) (*ParsedFunc, error) &#123;<br>
f, err := parse(text)<br>
if err != nil &#123;<br>
    return nil, err<br>
&#125;<br>
return &ParsedFunc&#123;text: text, eval: f&#125;, nil<br>
&#125;<br>
<br>
func (f *ParsedFunc) Eval(x float64) float64 &#123; return f.eval(x) &#125;<br>
func (f *ParsedFunc) String() string         &#123; return f.text &#125;` <br>
<br>
`drawer`  包：<br>
<br>
`import (<br>
"image"<br>
<br>
"golang.org/x/talks/content/2013/bestpractices/funcdraw/parser"<br>
)<br>
<br>
// Draw draws an image showing a rendering of the passed ParsedFunc. func DrawParsedFunc(f parser.ParsedFunc) image.Image &#123; <br>
</pre><br>
使用接口类型，避免依赖。<br>
<pre class="prettyprint">import "image"<br>
<br>
// Function represent a drawable mathematical function. type Function interface &#123;<br>
Eval(float64) float64<br>
&#125;<br>
<br>
// Draw draws an image showing a rendering of the passed Function. func Draw(f Function) image.Image &#123; <br>
</pre><br>
<strong>测试</strong>：接口类型比具体类型更容易测试。<br>
<pre class="prettyprint">package drawer<br>
<br>
import (<br>
"math"<br>
"testing"<br>
)<br>
<br>
type TestFunc func(float64) float64<br>
<br>
func (f TestFunc) Eval(x float64) float64 &#123; return f(x) &#125;<br>
<br>
var (<br>
ident = TestFunc(func(x float64) float64 &#123; return x &#125;)<br>
sin   = TestFunc(math.Sin)<br>
)<br>
<br>
func TestDraw_Ident(t *testing.T) &#123;<br>
m := Draw(ident)<br>
// Verify obtained image.<br>
</pre><br>
<h4>避免在内部使用并发</h4><pre class="prettyprint">func doConcurrently(job string, err chan error) &#123;<br>
go func() &#123;<br>
    fmt.Println("doing job", job)<br>
    time.Sleep(1 * time.Second)<br>
    err <- errors.New("something went wrong!")<br>
&#125;()<br>
&#125;<br>
<br>
func main() &#123;<br>
jobs := []string&#123;"one", "two", "three"&#125;<br>
<br>
errc := make(chan error)<br>
for _, job := range jobs &#123;<br>
    doConcurrently(job, errc)<br>
&#125;<br>
for _ = range jobs &#123;<br>
    if err := <-errc; err != nil &#123;<br>
        fmt.Println(err)<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
如果这样做，那如果我们想同步调用  <code class="prettyprint">doConcurrently</code>  该如何做？<br>
<pre class="prettyprint">func do(job string) error &#123;<br>
fmt.Println("doing job", job)<br>
time.Sleep(1 * time.Second)<br>
return errors.New("something went wrong!")<br>
&#125;<br>
<br>
func main() &#123;<br>
jobs := []string&#123;"one", "two", "three"&#125;<br>
<br>
errc := make(chan error)<br>
for _, job := range jobs &#123;<br>
    go func(job string) &#123;<br>
        errc <- do(job)<br>
    &#125;(job)<br>
&#125;<br>
for _ = range jobs &#123;<br>
    if err := <-errc; err != nil &#123;<br>
        fmt.Println(err)<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
对外暴露同步的函数，这样并发调用时也是容易的，同样也满足同步调用。<br>
<h3>最佳的并发实践</h3><h4>使用 Goroutine 管理状态</h4>Goroutine 之间使用一个 “通道” 或带有通道字段的 “结构体” 来通信。<br>
<pre class="prettyprint">type Server struct&#123; quit chan bool &#125;<br>
<br>
func NewServer() *Server &#123;<br>
s := &Server&#123;make(chan bool)&#125;<br>
go s.run()<br>
return s<br>
&#125;<br>
<br>
func (s *Server) run() &#123;<br>
for &#123;<br>
    select &#123;<br>
    case <-s.quit:<br>
        fmt.Println("finishing task")<br>
        time.Sleep(time.Second)<br>
        fmt.Println("task done")<br>
        s.quit <- true<br>
        return<br>
    case <-time.After(time.Second):<br>
        fmt.Println("running task")<br>
    &#125;<br>
&#125;<br>
&#125;<br>
<br>
func (s *Server) Stop() &#123;<br>
fmt.Println("server stopping")<br>
s.quit <- true<br>
<-s.quit<br>
fmt.Println("server stopped")<br>
&#125;<br>
<br>
func main() &#123;<br>
s := NewServer()<br>
time.Sleep(2 * time.Second)<br>
s.Stop()<br>
&#125; <br>
</pre><br>
<h4>使用带缓冲的通道避免 Goroutine 泄露</h4><pre class="prettyprint">func sendMsg(msg, addr string) error &#123;<br>
conn, err := net.Dial("tcp", addr)<br>
if err != nil &#123;<br>
    return err<br>
&#125;<br>
defer conn.Close()<br>
_, err = fmt.Fprint(conn, msg)<br>
return err<br>
&#125;<br>
<br>
func main() &#123;<br>
addr := []string&#123;"localhost:8080", "http://google.com"&#125;<br>
err := broadcastMsg("hi", addr)<br>
<br>
time.Sleep(time.Second)<br>
<br>
if err != nil &#123;<br>
    fmt.Println(err)<br>
    return<br>
&#125;<br>
fmt.Println("everything went fine")<br>
&#125;<br>
<br>
func broadcastMsg(msg string, addrs []string) error &#123;<br>
errc := make(chan error)<br>
for _, addr := range addrs &#123;<br>
    go func(addr string) &#123;<br>
        errc <- sendMsg(msg, addr)<br>
        fmt.Println("done")<br>
    &#125;(addr)<br>
&#125;<br>
<br>
for _ = range addrs &#123;<br>
    if err := <-errc; err != nil &#123;<br>
        return err<br>
    &#125;<br>
&#125;<br>
return nil<br>
&#125; <br>
</pre><br>
这段代码有个问题，如果提前返回了  <code class="prettyprint">err</code>  变量，<code class="prettyprint">errc</code>  通道将不会被读取，因此 Goroutine 将会阻塞。<br>
<br><strong>总结</strong>：<br>
<ul><li>在写入通道时 Goroutine 被阻塞。</li><li>Goroutine 持有对通道的引用。</li><li>通道不会被 gc 回收。</li></ul><br>
<br>使用缓冲通道解决 Goroutine 阻塞问题。<br>
<pre class="prettyprint">func broadcastMsg(msg string, addrs []string) error &#123;<br>
errc := make(chan error, len(addrs))<br>
for _, addr := range addrs &#123;<br>
    go func(addr string) &#123;<br>
        errc <- sendMsg(msg, addr)<br>
        fmt.Println("done")<br>
    &#125;(addr)<br>
&#125;<br>
<br>
for _ = range addrs &#123;<br>
    if err := <-errc; err != nil &#123;<br>
        return err<br>
    &#125;<br>
&#125;<br>
return nil<br>
&#125; <br>
</pre><br>
如果我们不能预知通道的缓冲大小，也称容量，那该怎么办？<br>
<br>创建一个传递退出状态的通道来避免 Goroutine 的泄露。<br>
<pre class="prettyprint">func broadcastMsg(msg string, addrs []string) error &#123;<br>
errc := make(chan error)<br>
quit := make(chan struct&#123;&#125;)<br>
<br>
defer close(quit)<br>
<br>
for _, addr := range addrs &#123;<br>
    go func(addr string) &#123;<br>
        select &#123;<br>
        case errc <- sendMsg(msg, addr):<br>
            fmt.Println("done")<br>
        case <-quit:<br>
            fmt.Println("quit")<br>
        &#125;<br>
    &#125;(addr)<br>
&#125;<br>
<br>
for _ = range addrs &#123;<br>
    if err := <-errc; err != nil &#123;<br>
        return err<br>
    &#125;<br>
&#125;<br>
return nil<br>
&#125; <br>
</pre><br>
参考：<br>
<br><a href="https://talks.golang.org/2013/bestpractices.slide#1" rel="nofollow" target="_blank">https://talks.golang.org/2013/ ... e%231</a><br>
<br><a href="https://www.youtube.com/watch?v=8D3Vmm1BGoY" rel="nofollow" target="_blank">https://www.youtube.com/watch?v=8D3Vmm1BGoY</a><br>
<br>原文链接：<a href="https://printlove.cn/posts/go/2/" rel="nofollow" target="_blank">https://printlove.cn/posts/go/2/</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            