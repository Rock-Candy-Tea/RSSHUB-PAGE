
---
title: '.NET Core Session源码探究'
categories: 
 - 编程
 - 码农网
 - 最新
headimg: 'https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2020/06/net-core2.jpg'
author: 码农网
comments: false
date: Tue, 09 Jun 2020 14:07:19 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2020/06/net-core2.jpg'
---

<div>   
<h2 id="2557204724">前言</h2>
<p>随着互联网的兴起,技术的整体架构设计思路有了质的提升，曾经Web开发必不可少的内置对象Session已经被慢慢的遗弃。主要原因有两点，一是Session依赖Cookie存放SessionID，即使不通过Cookie传递，也要依赖在请求参数或路径上携带Session标识，对于目前前后端分离项目来说操作起来限制很大，比如跨域问题。二是Session数据跨服务器同步问题，现在基本上项目都使用<span class="wp_keywordlink"><a href="http://www.codeceo.com/article/balanced-algorithm.html" title="负载均衡" target="_blank">负载均衡</a></span>技术，Session同步存在一定的弊端，虽然可以借助Redis或者其他存储系统实现中心化存储，但是略显鸡肋。虽然存在一定的弊端，但是在.NET Core也并没有抛弃它，而且结合了更好的实现方式提升了设计思路。接下来我们通过分析源码的方式，大致了解下新的工作方式。</p>
<p><img class="aligncenter size-full wp-image-57207" title="net-core2" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2020/06/net-core2.jpg" alt width="562" height="300" referrerpolicy="no-referrer"></p>
<h2 id="1781659463">Session如何使用</h2>
<p>.NET Core的Session使用方式和传统的使用方式有很大的差别，首先它依赖存储系统IDistributedCache来存储数据，其次它依赖SessionMiddleware为每一次请求提供具体的实例。所以使用Session之前需要配置一些操作，详细介绍可参阅微软官方文档<a href="https://docs.microsoft.com/en-us/aspnet/core/fundamentals/app-state?view=aspnetcore-3.1#session-state">会话状态</a>。大致配置流程，如下：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public class Startup
&#123;
    public Startup(IConfiguration configuration)
    &#123;
        Configuration = configuration;
    &#125;
    public IConfiguration Configuration &#123; get; &#125;

    public void ConfigureServices(IServiceCollection services)
    &#123;
        services.AddDistributedMemoryCache();
        services.AddSession(options =>
        &#123;
            options.IdleTimeout = TimeSpan.FromSeconds(10);
            options.Cookie.HttpOnly = true;
            options.Cookie.IsEssential = true;
        &#125;);
    &#125;

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    &#123;
        app.UseSession();
    &#125;
&#125;</pre>
<h3 id="2257728645">Session注入代码分析</h3>
<p>注册的地方设计到了两个扩展方法AddDistributedMemoryCache和AddSession.其中AddDistributedMemoryCache这是借助IDistributedCache为Session数据提供存储，AddSession是Session实现的核心的注册操作。</p>
<h3 id="2262271722">IDistributedCache提供存储</h3>
<p>上面的示例中示例中使用的是基于本地内存存储的方式，也可以使用IDistributedCache针对Redis和数据库存储的扩展方法。实现也非常简单就是给IDistributedCache注册存储操作实例</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public static IServiceCollection AddDistributedMemoryCache(this IServiceCollection services)
&#123;
    if (services == null)
    &#123;
        throw new ArgumentNullException(nameof(services));
    &#125;
    services.AddOptions();
    services.TryAdd(ServiceDescriptor.Singleton<IDistributedCache, MemoryDistributedCache>());
    return services;
&#125;</pre>
<p>关于IDistributedCache的其他使用方式请参阅官方文档的<a href="https://docs.microsoft.com/en-us/aspnet/core/performance/caching/distributed?view=aspnetcore-3.1">分布式缓存篇</a>，关于分布式缓存源码实现可以通过<a href="https://github.com/dotnet/extensions/tree/v3.1.4/src/Caching">Cache的Github地址</a>自行查阅。</p>
<h3 id="3678161260">AddSession核心操作</h3>
<p>AddSession是Session实现的核心的注册操作，具体实现代码来自扩展类<a href="https://github.com/dotnet/aspnetcore/blob/v3.1.4/src/Middleware/Session/src/SessionServiceCollectionExtensions.cs">SessionServiceCollectionExtensions</a>，AddSession扩展方法大致实现如下：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public static IServiceCollection AddSession(this IServiceCollection services)
&#123;
    if (services == null)
    &#123;
        throw new ArgumentNullException(nameof(services));
    &#125;
    services.TryAddTransient<ISessionStore, DistributedSessionStore>();
    services.AddDataProtection();
    return services;
&#125;</pre>
<p>这个方法就做了两件事，一个是注册了Session的具体操作，另一个是添加了数据保护保护条例支持。和Session真正相关的其实只有ISessionStore，话不多说，继续向下看<a href="https://github.com/dotnet/aspnetcore/blob/v3.1.4/src/Middleware/Session/src/DistributedSessionStore.cs">DistributedSessionStore实现</a></p>
<pre class="brush: csharp; gutter: true; first-line: 1">public class DistributedSessionStore : ISessionStore
&#123;
    private readonly IDistributedCache _cache;
    private readonly ILoggerFactory _loggerFactory;

    public DistributedSessionStore(IDistributedCache cache, ILoggerFactory loggerFactory)
    &#123;
        if (cache == null)
        &#123;
            throw new ArgumentNullException(nameof(cache));
        &#125;
        if (loggerFactory == null)
        &#123;
            throw new ArgumentNullException(nameof(loggerFactory));
        &#125;
        _cache = cache;
        _loggerFactory = loggerFactory;
    &#125;
    public ISession Create(string sessionKey, TimeSpan idleTimeout, TimeSpan ioTimeout, Func<bool> tryEstablishSession, bool isNewSessionKey)
    &#123;
        if (string.IsNullOrEmpty(sessionKey))
        &#123;
            throw new ArgumentException(Resources.ArgumentCannotBeNullOrEmpty, nameof(sessionKey));
        &#125;
        if (tryEstablishSession == null)
        &#123;
            throw new ArgumentNullException(nameof(tryEstablishSession));
        &#125;
        return new DistributedSession(_cache, sessionKey, idleTimeout, ioTimeout, tryEstablishSession, _loggerFactory, isNewSessionKey);
    &#125;
&#125;</pre>
<p>这里的实现也非常简单就是创建Session实例DistributedSession，在这里我们就可以看出创建Session是依赖IDistributedCache的,这里的sessionKey其实是SessionID,当前会话唯一标识。继续向下找到<a href="https://github.com/dotnet/aspnetcore/blob/v3.1.4/src/Middleware/Session/src/DistributedSession.cs">DistributedSession实现</a>,这里的代码比较多，因为这是封装Session操作的实现类。老规矩先找到我们最容易下手的Get方法：</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public bool TryGetValue(string key, out byte[] value)
&#123;
    Load();
    return _store.TryGetValue(new EncodedKey(key), out value);
&#125;</pre>
<p>我们看到调用TryGetValue之前先调用了Load方法，这是内部的私有方法</p>
<pre class="brush: csharp; gutter: true; first-line: 1">private void Load()
&#123;
    //判断当前会话中有没有加载过数据
    if (!_loaded)
    &#123;
        try
        &#123;
            //根据会话唯一标识在IDistributedCache中获取数据
            var data = _cache.Get(_sessionKey);
            if (data != null)
            &#123;
                //由于存储的是按照特定的规则得到的二进制数据，所以获取的时候要将数据反序列化
                Deserialize(new MemoryStream(data));
            &#125;
            else if (!_isNewSessionKey)
            &#123;
                _logger.AccessingExpiredSession(_sessionKey);
            &#125;
            //是否可用标识
            _isAvailable = true;
        &#125;
        catch (Exception exception)
        &#123;
            _logger.SessionCacheReadException(_sessionKey, exception);
            _isAvailable = false;
            _sessionId = string.Empty;
            _sessionIdBytes = null;
            _store = new NoOpSessionStore();
        &#125;
        finally
        &#123;
           //将数据标识设置为已加载状态
            _loaded = true;
        &#125;
    &#125;
&#125;

private void Deserialize(Stream content)
&#123;
    if (content == null || content.ReadByte() != SerializationRevision)
    &#123;
        // Replace the un-readable format.
        _isModified = true;
        return;
    &#125;

    int expectedEntries = DeserializeNumFrom3Bytes(content);
    _sessionIdBytes = ReadBytes(content, IdByteCount);

    for (int i = 0; i < expectedEntries; i++)
    &#123;
        int keyLength = DeserializeNumFrom2Bytes(content);
        //在存储的数据中按照规则获取存储设置的具体key
        var key = new EncodedKey(ReadBytes(content, keyLength));
        int dataLength = DeserializeNumFrom4Bytes(content);
        //将反序列化之后的数据存储到_store
        _store[key] = ReadBytes(content, dataLength);
    &#125;

    if (_logger.IsEnabled(LogLevel.Debug))
    &#123;
        _sessionId = new Guid(_sessionIdBytes).ToString();
        _logger.SessionLoaded(_sessionKey, _sessionId, expectedEntries);
    &#125;
&#125;</pre>
<p>通过上面的代码我们可以得知Get数据之前之前先Load数据,Load其实就是在IDistributedCache中获取数据然后存储到了_store中，通过当前类源码可知_store是本地字典，也就是说Session直接获取的其实是本地字典里的数据。</p>
<pre class="brush: csharp; gutter: true; first-line: 1">private IDictionary<EncodedKey, byte[]> _store；</pre>
<p>这里其实产生两点疑问:</p>
<ul>
<li>1.针对每个会话存储到IDistributedCache的其实都在一个Key里，就是以当前会话唯一标识为key的value里,为什么没有采取组合会话key单独存储。</li>
<li>2.每次请求第一次操作Session，都会把IDistributedCache里针对当前会话的数据全部加载到本地字典里，一般来说每次会话操作Session的次数并不会很多，感觉并不会节约性能。</li>
</ul>
<p>接下来我们在再来查看另一个我们比较熟悉的方法Set方法</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public void Set(string key, byte[] value)
&#123;
    if (value == null)
    &#123;
        throw new ArgumentNullException(nameof(value));
    &#125;
    if (IsAvailable)
    &#123;
        //存储的key是被编码过的
        var encodedKey = new EncodedKey(key);
        if (encodedKey.KeyBytes.Length > KeyLengthLimit)
        &#123;
            throw new ArgumentOutOfRangeException(nameof(key),
                Resources.FormatException_KeyLengthIsExceeded(KeyLengthLimit));
        &#125;
        if (!_tryEstablishSession())
        &#123;
            throw new InvalidOperationException(Resources.Exception_InvalidSessionEstablishment);
        &#125;
        //是否修改过标识
        _isModified = true;
        //将原始内容转换为byte数组
        byte[] copy = new byte[value.Length];
        Buffer.BlockCopy(src: value, srcOffset: 0, dst: copy, dstOffset: 0, count: value.Length);
        //将数据存储到本地字典_store
        _store[encodedKey] = copy;
    &#125;
&#125;</pre>
<p>这里我们可以看到Set方法并没有将数据放入到存储系统，只是放入了本地字典里。我们再来看其他方法</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public void Remove(string key)
&#123;
    Load();
    _isModified |= _store.Remove(new EncodedKey(key));
&#125;

public void Clear()
&#123;
    Load();
    _isModified |= _store.Count > 0;
    _store.Clear();
&#125;</pre>
<p>这些方法都没有对存储系统DistributedCache里的数据进行操作，都只是操作从存储系统Load到本地的字典数据。那什么地方进行的存储呢，也就是说我们要找到调用_cache.Set方法的地方，最后在<a href="https://github.com/dotnet/aspnetcore/blob/v3.1.4/src/Middleware/Session/src/DistributedSession.cs#L236">这个地方</a>找到了Set方法,而且看这个方法名就知道是提交Session数据的地方</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public async Task CommitAsync(CancellationToken cancellationToken = default)
&#123;
    //超过_ioTimeout CancellationToken将自动取消
    using (var timeout = new CancellationTokenSource(_ioTimeout))
    &#123;
        var cts = CancellationTokenSource.CreateLinkedTokenSource(timeout.Token, cancellationToken);
        //数据被修改过
        if (_isModified)
        &#123;
            if (_logger.IsEnabled(LogLevel.Information))
            &#123;
                try
                &#123;
                    cts.Token.ThrowIfCancellationRequested();
                    var data = await _cache.GetAsync(_sessionKey, cts.Token);
                    if (data == null)
                    &#123;
                        _logger.SessionStarted(_sessionKey, Id);
                    &#125;
                &#125;
                catch (OperationCanceledException)
                &#123;
                &#125;
                catch (Exception exception)
                &#123;
                    _logger.SessionCacheReadException(_sessionKey, exception);
                &#125;
            &#125;
            var stream = new MemoryStream();
            //将_store字典里的数据写到stream里
            Serialize(stream);
            try
            &#123;
                cts.Token.ThrowIfCancellationRequested();
                //将读取_store的流写入到DistributedCache存储里
                await _cache.SetAsync(
                    _sessionKey,
                    stream.ToArray(),
                    new DistributedCacheEntryOptions().SetSlidingExpiration(_idleTimeout),
                    cts.Token);
                _isModified = false;
                _logger.SessionStored(_sessionKey, Id, _store.Count);
            &#125;
            catch (OperationCanceledException oex)
            &#123;
                if (timeout.Token.IsCancellationRequested)
                &#123;
                    _logger.SessionCommitTimeout();
                    throw new OperationCanceledException("Timed out committing the session.", oex, timeout.Token);
                &#125;
                throw;
            &#125;
        &#125;
        else
        &#123;
            try
            &#123;
                await _cache.RefreshAsync(_sessionKey, cts.Token);
            &#125;
            catch (OperationCanceledException oex)
            &#123;
                if (timeout.Token.IsCancellationRequested)
                &#123;
                    _logger.SessionRefreshTimeout();
                    throw new OperationCanceledException("Timed out refreshing the session.", oex, timeout.Token);
                &#125;
                throw;
            &#125;
        &#125;
    &#125;
&#125;

private void Serialize(Stream output)
&#123;
    output.WriteByte(SerializationRevision);
    SerializeNumAs3Bytes(output, _store.Count);
    output.Write(IdBytes, 0, IdByteCount);
    //将_store字典里的数据写到Stream里
    foreach (var entry in _store)
    &#123;
        var keyBytes = entry.Key.KeyBytes;
        SerializeNumAs2Bytes(output, keyBytes.Length);
        output.Write(keyBytes, 0, keyBytes.Length);
        SerializeNumAs4Bytes(output, entry.Value.Length);
        output.Write(entry.Value, 0, entry.Value.Length);
    &#125;
&#125;</pre>
<p>那么问题来了当前类里并没有地方调用CommitAsync，那么到底是在什么地方调用的该方法呢？姑且别着急，我们之前说过使用Session的三要素，现在才说了两个，还有一个UseSession的中间件没有提及到呢。</p>
<h2 id="4186570368">UseSession中间件</h2>
<p>通过上面注册的相关方法我们大概了解到了Session的工作原理。接下来我们查看UseSession中间件里的代码，探究这里究竟做了什么操作。我们找到UseSession方法所在的地方<a href="https://github.com/dotnet/aspnetcore/blob/v3.1.4/src/Middleware/Session/src/SessionMiddlewareExtensions.cs">SessionMiddlewareExtensions</a>找到第一个方法</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public static IApplicationBuilder UseSession(this IApplicationBuilder app)
&#123;
    if (app == null)
    &#123;
        throw new ArgumentNullException(nameof(app));
    &#125;
    return app.UseMiddleware<SessionMiddleware>();
&#125;</pre>
<p>SessionMiddleware的源码</p>
<pre class="brush: csharp; gutter: true; first-line: 1">public class SessionMiddleware
&#123;
  private static readonly RandomNumberGenerator CryptoRandom = RandomNumberGenerator.Create();
  private const int SessionKeyLength = 36; // "382c74c3-721d-4f34-80e5-57657b6cbc27"
  private static readonly Func<bool> ReturnTrue = () => true;
  private readonly RequestDelegate _next;
  private readonly SessionOptions _options;
  private readonly ILogger _logger;
  private readonly ISessionStore _sessionStore;
  private readonly IDataProtector _dataProtector;

  public SessionMiddleware(
      RequestDelegate next,
      ILoggerFactory loggerFactory,
      IDataProtectionProvider dataProtectionProvider,
      ISessionStore sessionStore,
      IOptions<SessionOptions> options)
  &#123;
      if (next == null)
      &#123;
          throw new ArgumentNullException(nameof(next));
      &#125;
      if (loggerFactory == null)
      &#123;
          throw new ArgumentNullException(nameof(loggerFactory));
      &#125;
      if (dataProtectionProvider == null)
      &#123;
          throw new ArgumentNullException(nameof(dataProtectionProvider));
      &#125;
      if (sessionStore == null)
      &#123;
          throw new ArgumentNullException(nameof(sessionStore));
      &#125;
      if (options == null)
      &#123;
          throw new ArgumentNullException(nameof(options));
      &#125;
      _next = next;
      _logger = loggerFactory.CreateLogger<SessionMiddleware>();
      _dataProtector = dataProtectionProvider.CreateProtector(nameof(SessionMiddleware));
      _options = options.Value;
     //Session操作类在这里被注入的
      _sessionStore = sessionStore;
  &#125;

  public async Task Invoke(HttpContext context)
  &#123;
      var isNewSessionKey = false;
      Func<bool> tryEstablishSession = ReturnTrue;
      var cookieValue = context.Request.Cookies[_options.Cookie.Name];
      var sessionKey = CookieProtection.Unprotect(_dataProtector, cookieValue, _logger);
      //会话首次建立
      if (string.IsNullOrWhiteSpace(sessionKey) || sessionKey.Length != SessionKeyLength)
      &#123;
          //将会话唯一标识通过Cookie返回到客户端
          var guidBytes = new byte[16];
          CryptoRandom.GetBytes(guidBytes);
          sessionKey = new Guid(guidBytes).ToString();
          cookieValue = CookieProtection.Protect(_dataProtector, sessionKey);
          var establisher = new SessionEstablisher(context, cookieValue, _options);
          tryEstablishSession = establisher.TryEstablishSession;
          isNewSessionKey = true;
      &#125;
      var feature = new SessionFeature();
      //创建Session
      feature.Session = _sessionStore.Create(sessionKey, _options.IdleTimeout, _options.IOTimeout, tryEstablishSession, isNewSessionKey);
      //放入到ISessionFeature,给HttpContext中的Session数据提供具体实例
      context.Features.Set<ISessionFeature>(feature);
      try
      &#123;
          await _next(context);
      &#125;
      finally
      &#123;
          //置空为了在请求结束后可以回收掉Session
          context.Features.Set<ISessionFeature>(null);
          if (feature.Session != null)
          &#123;
              try
              &#123;
                  //请求完成后提交保存Session字典里的数据到DistributedCache存储里
                  await feature.Session.CommitAsync();
              &#125;
              catch (OperationCanceledException)
              &#123;
                  _logger.SessionCommitCanceled();
              &#125;
              catch (Exception ex)
              &#123;
                  _logger.ErrorClosingTheSession(ex);
              &#125;
          &#125;
      &#125;
  &#125;

  private class SessionEstablisher
  &#123;
      private readonly HttpContext _context;
      private readonly string _cookieValue;
      private readonly SessionOptions _options;
      private bool _shouldEstablishSession;

      public SessionEstablisher(HttpContext context, string cookieValue, SessionOptions options)
      &#123;
          _context = context;
          _cookieValue = cookieValue;
          _options = options;
          context.Response.OnStarting(OnStartingCallback, state: this);
      &#125;

      private static Task OnStartingCallback(object state)
      &#123;
          var establisher = (SessionEstablisher)state;
          if (establisher._shouldEstablishSession)
          &#123;
              establisher.SetCookie();
          &#125;
          return Task.FromResult(0);
      &#125;

      private void SetCookie()
      &#123;
          //会话标识写入到Cookie操作
          var cookieOptions = _options.Cookie.Build(_context);
          var response = _context.Response;
          response.Cookies.Append(_options.Cookie.Name, _cookieValue, cookieOptions);
          var responseHeaders = response.Headers;
          responseHeaders[HeaderNames.CacheControl] = "no-cache";
          responseHeaders[HeaderNames.Pragma] = "no-cache";
          responseHeaders[HeaderNames.Expires] = "-1";
      &#125;

      internal bool TryEstablishSession()
      &#123;
          return (_shouldEstablishSession |= !_context.Response.HasStarted);
      &#125;
  &#125;
&#125;</pre>
<p>通过SessionMiddleware中间件里的代码我们了解到了每次请求Session的创建，以及Session里的数据保存到DistributedCache都是在这里进行的。不过这里仍存在一个疑问由于调用CommitAsync是在中间件执行完成后统一进行存储的，也就是说中途对Session进行的Set Remove Clear的操作都是在Session方法的本地字典里进行的，并没有同步到DistributedCache里，如果中途出现程序异常结束的情况下，保存到Session里的数据，并没有真正的存储下来，会出现丢失的情况，不知道在设计这部分逻辑的时候是出于什么样的考虑。</p>
<h2 id="72240361">总结</h2>
<p>通过阅读Session相关的部分源码大致了解了Session的原理，工作三要素，IDistributedCache存储Session里的数据，SessionStore是Session的实现类，UseSession是Session被创建到当前请求的地方。同时也留下了几点疑问</p>
<ul>
<li>针对每个会话存储到IDistributedCache的其实都在一个Key里，就是以当前会话唯一标识为key的value里,为什么没有采取组合会话key单独存储。</li>
<li>每次请求第一次操作Session，都会把IDistributedCache里针对当前会话的数据全部加载到本地字典里，一般来说每次会话操作Session的次数并不会很多，感觉并不会节约性能。</li>
<li>调用CommitAsync是在中间件执行完成后统一进行存储的，也就是说中途对Session进行的Set Remove Clear的操作都是在Session方法的本地字典里进行的，并没有同步到DistributedCache里，如果中途出现程序异常结束的情况下，保存到Session里的数据，并没有真正的存储下来，会出现丢失的情况。</li>
</ul>
<p>对于以上疑问，不知道是个人理解不足，还是在设计的时候出于别的考虑。欢迎在评论区多多沟通交流，希望能从大家那里得到更好的解释和答案。</p>


<a id="soft-link" name="soft-link" href="http://www.codeceo.com/article/undefined"></a>




<!--开源软件资源链接-->
<!--开源软件资源链接结束-->







  
</div>
            