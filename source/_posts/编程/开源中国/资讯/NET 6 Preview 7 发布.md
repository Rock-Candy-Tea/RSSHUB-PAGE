
---
title: '.NET 6 Preview 7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=277'
author: 开源中国
comments: false
date: Wed, 18 Aug 2021 08:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=277'
---

<div>   
<div class="content">
                                                                                            <p> .NET 6 Preview 7 现已。这是发布 RC 版本之前的最后一次预览。本次更新包括对各种功能的最后一点润色，以及一次性的大型功能发布，并且受 Visual Studio 2022 Preview 3 支持。</p> 
<h4>.NET SDK：现代化的 C# 项目模板</h4> 
<p>该版本更新了 .NET SDK 模板以使用最新的 C# 语言功能和模式。新模板中使用了以下语言功能：</p> 
<ul> 
 <li>Top-level 语句</li> 
 <li>异步 Main</li> 
 <li>全局 using 指令（通过 SDK 驱动的默认值）</li> 
 <li>文件范围的命名空间</li> 
 <li>目标类型的新表达式</li> 
 <li>可空引用类型</li> 
</ul> 
<p>通过项目模板启用这些功能，新代码可以从启用这些功能开始，但升级时现有代码不受影响。</p> 
<pre><code>var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

if (app.Environment.IsDevelopment())
&#123;
    app.UseDeveloperExceptionPage();
&#125;

app.MapGet("/", () => "Hello World!");

app.Run();</code></pre> 
<h4>可用于无效信息的反射 API</h4> 
<p>可空引用类型是编写可靠代码的重要特性，它非常适合编写代码，但不适用于检查。新的反射 API 使用户能够确定给定方法的参数和返回值的可空性性质。 对于上下文，该版本在 .NET 5 中向 .NET 库添加了可空性的注释（并在 .NET 6 中完成），并且正在对 ASP.NET Core 做同样的事情。可空性信息使用自定义属性保存在元数据中，原则上，任何人都可以读取自定义属性。</p> 
<pre><code>class Data
&#123;
    public string?[] ArrayField;
    public (string?, object) TupleField;
&#125;
private void Print()
&#123;
    Type type = typeof(Data);
    FieldInfo arrayField = type.GetField("ArrayField");
    FieldInfo tupleField = type.GetField("TupleField");

    NullabilityInfoContext context = new ();

    NullabilityInfo arrayInfo = context.Create(arrayField);
    Console.WriteLine(arrayInfo.ReadState);        // NotNull
    Console.WriteLine(arrayInfo.Element.State);    // Nullable

    NullabilityInfo tupleInfo = context.Create(tupleField);
    Console.WriteLine(tupleInfo.ReadState);                      // NotNull
    Console.WriteLine(tupleInfo.GenericTypeArguments [0].State); // Nullable
    Console.WriteLine(tupleInfo.GenericTypeArguments [1].State); // NotNull
&#125;</code></pre> 
<h4>ZipFile 获得 Unix 文件权限</h4> 
<p>System.IO.Compression.ZipFile 类现在在创建和设置文件权限期间捕获 Unix 文件权限。此更改允许通过 zip 存档来回传送可执行文件，这意味着用户不再需要在解压缩 zip 存档后修改文件权限以使文件可执行。如果 zip 存档不包含文件权限，则提取的文件将获得默认文件权限，就像任何其他文件一样新创建的文件。</p> 
<h4>.NET 7 早期功能预览：通用数学</h4> 
<p>该版本在 .NET 6 中预览的其中一项功能是静态抽象接口成员，这允许用户在接口中定义静态抽象方法（包括运算符）。例如，现在可以实现代数泛型方法。对于某些用户来说，此功能可能是今年最出色的改进，它可能是自 Span<T> 以来最重要的新型系统功能。以下示例采用 IEnumerable<T>，并且由于 T 被约束为 INumber<T>，因此能够对所有值求和。</p> 
<pre><code>public static T Sum<T>(IEnumerable<T> values)
    where T : INumber<T>
&#123;
    T result = T.Zero;

    foreach (var value in values)
    &#123;
        result += value;
    &#125;

    return result;
&#125;</code></pre> 
<h4>NativeMemory API</h4> 
<p>该版本添加了通过 System.Runtime.InteropServices.NativeMemory 公开的新本地内存分配 API，这些 API 与 malloc、free、realloc 和 calloc C API 等效，还包括用于进行对齐分配的 API。</p> 
<h4>System.Text.Json 序列化通知</h4> 
<p>System.Text.Json 序列化程序现在将通知作为（反）序列化操作的一部分公开，这对于默认值和验证很有用。要使用该功能，需要在 System.Text.Json.Serialization 命名空间内实现一个或多个接口 IJsonOnDeserialized、IJsonOnDeserializing、IJsonOnSerialized 或 IJsonOnSerializing。下面是一个在 JsonSerializer.Serialize() 和 JsonSerializer.Deserialize() 期间验证的示例，以确保 FirstName 属性不为空。</p> 
<pre><code>  public class Person : IJsonOnDeserialized, IJsonOnSerializing
  &#123;
      public string FirstName&#123; get; set; &#125;

      void IJsonOnDeserialized.OnDeserialized() => Validate(); // Call after deserialization
      void IJsonOnSerializing.OnSerializing() => Validate(); // Call before serialization

      private void Validate()
      &#123;
          if (FirstName is null)
          &#123;
              throw new InvalidOperationException("The 'FirstName' property cannot be 'null'.");
          &#125;
      &#125;
  &#125;</code></pre> 
<h4>W^X（write xor execute）支持所有平台和架构</h4> 
<p>运行时现在有一种模式，它不会同时创建或使用任何可写和可执行的内存页面，所有可执行内存都映射为只读。此功能已在 macOS（适用于 Apple Silicon）上和其它平台启用。此前在 Apple Silicon 机器上，同时可写和可执行的内存映射是被禁止的。</p> 
<p>在这些平台上，可执行代码的生成/修改是通过单独的读写内存映射完成的，而这些映射是在与可执行代码地址不同的虚拟内存地址处创建的，并且仅在执行写入时存在很短的时间。例如，JIT 现在将代码生成到暂存缓冲区中，在整个方法被 jitt 之后，使用单个内存复制函数调用将代码复制到可执行内存中。并且可写映射生命周期仅跨越内存复制的时间。</p> 
<p>用户可以通过将环境变量 DOTNET_EnableWriteXorExecute 设置为 1 来启用此新功能。此功能目前是可选的，因为它具有启动回归（Apple Silicon 除外）。预计在 .NET 7 中解决性能回归问题，并在那时默认启用该功能。</p> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-net-6-preview-7%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            