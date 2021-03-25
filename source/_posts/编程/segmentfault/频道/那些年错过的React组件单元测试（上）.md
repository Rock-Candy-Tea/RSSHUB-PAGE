
---
title: '那些年错过的React组件单元测试（上）'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: 'https://segmentfault.com/img/remote/1460000039710018'
author: segmentfault
comments: false
date: 2021-03-25 04:15:50
thumbnail: 'https://segmentfault.com/img/remote/1460000039710018'
---

<div>   
<h2>🏂 写在前面</h2><p>关于前端单元测试，其实两年前我就已经关注了，但那时候只是简单的知道<code>断言</code>，想着也不是太难的东西，项目中也没有用到，然后就想当然的认为自己就会了。</p><p>两年后的今天，部门要对以往的项目补加单元测试。真到了开始着手的时候，却懵了 😂</p><p>我以为的我以为却把自己给坑了，我发现自己对于前端单元测试一无所知。然后我翻阅了大量的文档，发现基于<code>dva</code>的单元测试文档比较少，因此在有了一番实践之后，我梳理了几篇文章，希望对于想<code>使用 Jest 进行 React + Dva + Antd 单元测试</code>的你能有所帮助。文章内容力求深入浅出，浅显易懂～</p><blockquote>介于内容全部收在一篇会太长，计划分为两篇，本篇是第一篇，主要介绍如何快速上手<code>jest</code>以及在实战中常用的功能及<code>api</code></blockquote><h2>🏈 前端自动化测试产生的背景</h2><p>在开始介绍<code>jest</code>之前，我想有必要简单阐述一下关于前端单元测试的一些基础信息。</p><ul><li>为什么要进行测试？<p>在 2021 年的今天，构建一个复杂的<code>web</code>应用对于我们来说，并非什么难事。因为有足够多优秀的的前端框架（比如 <code>React</code>，<code>Vue</code>）；以及一些易用且强大的<code>UI</code>库（比如 <code>Ant Design</code>，<code>Element UI</code>）为我们保驾护航，极大地缩短了应用构建的周期。但是快速迭代的过程中却产生了大量的问题：代码质量（可读性差、可维护性低、可扩展性低）低，频繁的产品需求变动（代码变动影响范围不可控）等。</p><p>因此单元测试的概念在前端领域应运而生，通过编写单元测试可以确保得到预期的结果，提高代码的可读性，如果依赖的组件有修改，受影响的组件也能在测试中及时发现错误。</p></li><li><p>测试类型又有哪些呢？</p><p>一般常见的有以下四种：</p><ul><li>单元测试</li><li>功能测试</li><li>集成测试</li><li>冒烟测试</li></ul></li><li><p>常见的开发模式呢？</p><ul><li><code>TDD</code>: 测试驱动开发</li><li><code>BDD</code>: 行为驱动测试</li></ul></li></ul><h2>🎮 技术方案</h2><p>针对项目本身使用的是<code>React + Dva + Antd</code>的技术栈，单元测试我们用的是<code>Jest + Enzyme</code>结合的方式。</p><h3><code>Jest</code></h3><p>关于<code>Jest</code>，我们参考一下其<a href="https://jestjs.io/zh-Hans/" rel="nofollow">Jest 官网</a>，它是<code>Facebook</code>开源的一个前端测试框架，主要用于<code>React</code>和<code>React Native</code>的单元测试，已被集成在<code>create-react-app</code>中。<code>Jest</code>特点：</p><ul><li>零配置</li><li>快照</li><li>隔离</li><li>优秀的 api</li><li>快速且安全</li><li>代码覆盖率</li><li>轻松模拟</li><li>优秀的报错信息</li></ul><h3><code>Enzyme</code></h3><p><code>Enzyme</code>是<code>Airbnb</code>开源的<code>React</code>测试工具库，提供了一套简洁强大的<code>API</code>，并内置<code>Cheerio</code>，同时实现了<code>jQuery</code>风格的方式进行<code>DOM</code>处理，开发体验十分友好。在开源社区有超高人气，同时也获得了<code>React</code>官方的推荐。</p><h2>📌 <code>Jest</code></h2><p>本篇文章我们着重来介绍一下<code>Jest</code>，也是我们整个<code>React单元测试</code>的根基。</p><h3>环境搭建</h3><h4>安装</h4><p>安装<code>Jest</code>、<code>Enzyme</code>。如果<code>React</code>的版本是<code>15</code>或者<code>16</code>，需要安装对应的<code>enzyme-adapter-react-15</code>和<code>enzyme-adapter-react-16</code>并配置。</p><pre><code class="js">/**
 * setup
 *
 */

import Enzyme from "enzyme"
import Adapter from "enzyme-adapter-react-16"
Enzyme.configure(&#123; adapter: new Adapter() &#125;)</code></pre><h4>jest.config.js</h4><p>可以运行<code>npx jest --init</code>在根目录生成配置文件<code>jest.config.js</code></p><pre><code>/*
 * For a detailed explanation regarding each configuration property, visit:
 * https://jestjs.io/docs/en/configuration.html
 */

module.exports = &#123;
  // All imported modules in your tests should be mocked automatically
  // automock: false,

  // Automatically clear mock calls and instances between every test
  clearMocks: true,

  // Indicates whether the coverage information should be collected while executing the test
  // collectCoverage: true,

  // An array of glob patterns indicating a set of files for which coverage information should be collected
  collectCoverageFrom: ["src/**/*.&#123;js,jsx,ts,tsx&#125;", "!src/**/*.d.ts"],

  // The directory where Jest should output its coverage files
  coverageDirectory: "coverage",

  // An array of regexp pattern strings used to skip coverage collection
  // coveragePathIgnorePatterns: [
  //   "/node_modules/"
  // ],


  // An array of directory names to be searched recursively up from the requiring module's location
  moduleDirectories: ["node_modules", "src"],

  // An array of file extensions your modules use
  moduleFileExtensions: ["js", "json", "jsx", "ts", "tsx"],


  // An array of regexp pattern strings, matched against all module paths before considered 'visible' to the module loader
  // modulePathIgnorePatterns: [],

  // Automatically reset mock state between every test
  // resetMocks: false,

  // Reset the module registry before running each individual test
  // resetModules: false,

  // Automatically restore mock state between every test
  // restoreMocks: false,

  // The root directory that Jest should scan for tests and modules within
  // rootDir: undefined,

  // A list of paths to directories that Jest should use to search for files in
  // roots: [
  //   "<rootDir>"
  // ],

  // The paths to modules that run some code to configure or set up the testing environment before each test
  // setupFiles: [],

  // A list of paths to modules that run some code to configure or set up the testing framework before each test
  setupFilesAfterEnv: [
    "./node_modules/jest-enzyme/lib/index.js",
    "<rootDir>/src/utils/testSetup.js",
  ],

  // The test environment that will be used for testing
  testEnvironment: "jest-environment-jsdom",

  // Options that will be passed to the testEnvironment
  // testEnvironmentOptions: &#123;&#125;,

  // The glob patterns Jest uses to detect test files
  testMatch: ["**/?(*.)+(spec|test).[tj]s?(x)"],

  // An array of regexp pattern strings that are matched against all test paths, matched tests are skipped
  // testPathIgnorePatterns: [
  //   "/node_modules/"
  // ],


  // A map from regular expressions to paths to transformers
  // transform: undefined,

  // An array of regexp pattern strings that are matched against all source file paths, matched files will skip transformation
  transformIgnorePatterns: ["/node_modules/", "\\.pnp\\.[^\\/]+$"],
&#125;
</code></pre><p>这里只是列举了常用的配置项：</p><ul><li><code>automock</code>: 告诉 Jest 所有的模块都自动从 mock 导入.</li><li><code>clearMocks</code>: 在每个测试前自动清理 mock 的调用和实例 instance</li><li><code>collectCoverage</code>: 是否收集测试时的覆盖率信息</li><li><code>collectCoverageFrom</code>: 生成测试覆盖报告时检测的覆盖文件</li><li><code>coverageDirectory</code>: Jest 输出覆盖信息文件的目录</li><li><code>coveragePathIgnorePatterns</code>: 排除出 coverage 的文件列表</li><li><code>coverageReporters</code>: 列出包含 reporter 名字的列表，而 Jest 会用他们来生成覆盖报告</li><li><code>coverageThreshold</code>: 测试可以允许通过的阈值</li><li><code>moduleDirectories</code>: 模块搜索路径</li><li><code>moduleFileExtensions</code>：代表支持加载的文件名</li><li><code>testPathIgnorePatterns</code>：用正则来匹配不用测试的文件</li><li><code>setupFilesAfterEnv</code>：配置文件，在运行测试案例代码之前，Jest 会先运行这里的配置文件来初始化指定的测试环境</li><li><code>testMatch</code>: 定义被测试的文件</li><li><code>transformIgnorePatterns</code>: 设置哪些文件不需要转译</li><li><code>transform</code>: 设置哪些文件中的代码是需要被相应的转译器转换成 Jest 能识别的代码，Jest 默认是能识别 JS 代码的，其他语言，例如 Typescript、CSS 等都需要被转译。</li></ul><h3>匹配器</h3><ul><li><code>toBe(value)</code>：使用 Object.is 来进行比较，如果进行浮点数的比较，要使用 toBeCloseTo</li><li><code>not</code>：取反</li><li><code>toEqual(value)</code>：用于对象的深比较</li><li><code>toContain(item)</code>：用来判断 item 是否在一个数组中，也可以用于字符串的判断</li><li><code>toBeNull(value)</code>：只匹配 null</li><li><code>toBeUndefined(value)</code>：只匹配 undefined</li><li><code>toBeDefined(value)</code>：与 toBeUndefined 相反</li><li><code>toBeTruthy(value)</code>：匹配任何语句为真的值</li><li><code>toBeFalsy(value)</code>：匹配任何语句为假的值</li><li><code>toBeGreaterThan(number)</code>： 大于</li><li><code>toBeGreaterThanOrEqual(number)</code>：大于等于</li><li><code>toBeLessThan(number)</code>：小于</li><li><code>toBeLessThanOrEqual(number)</code>：小于等于</li><li><code>toBeInstanceOf(class)</code>：判断是不是 class 的实例</li><li><code>resolves</code>：用来取出 promise 为 fulfilled 时包裹的值，支持链式调用</li><li><code>rejects</code>：用来取出 promise 为 rejected 时包裹的值，支持链式调用</li><li><code>toHaveBeenCalled()</code>：用来判断 mock function 是否被调用过</li><li><code>toHaveBeenCalledTimes(number)</code>：用来判断 mock function 被调用的次数</li><li><code>assertions(number)</code>：验证在一个测试用例中有 number 个断言被调用</li></ul><h3>命令行工具的使用</h3><p>在项目<code>package.json</code>文件添加如下<code>script</code>:</p><pre><code class="diff">"scripts": &#123;
    "start": "node bin/server.js",
    "dev": "node bin/server.js",
    "build": "node bin/build.js",
    "publish": "node bin/publish.js",
++  "test": "jest --watchAll",
&#125;,</code></pre><p>此时运行<code>npm run test</code>:<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039710018" alt title referrerpolicy="no-referrer"></span></p><p>我们发现有以下几种模式：</p><ul><li><code>f</code>: 只会测试之前没有通过的测试用例</li><li><code>o</code>: 只会测试关联的并且改变的文件（需要使用 git）（jest --watch 可以直接进入该模式）</li><li><code>p</code>: 测试文件名包含输入的名称的测试用例</li><li><code>t</code>: 测试用例的名称包含输入的名称的测试用例</li><li><code>a</code>: 运行全部测试用例</li></ul><p>在测试过程中，你可以切换适合的模式。</p><h3>钩子函数</h3><p>类似于 react 或者 vue 的生命周期，一共有四种：</p><ul><li><code>beforeAll()</code>：所有测试用例执行之前执行的方法</li><li><code>afterAll()</code>：所有测试用例跑完以后执行的方法</li><li><code>beforeEach()</code>：在每个测试用例执行之前需要执行的方法</li><li><code>afterEach()</code>：在每个测试用例执行完后执行的方法</li></ul><p>这里，我以项目中的一个基础 <code>demo</code> 来演示一下具体使用：</p><p><code>Counter.js</code></p><pre><code>export default class Counter &#123;
  constructor() &#123;
    this.number = 0
  &#125;
  addOne() &#123;
    this.number += 1
  &#125;
  minusOne() &#123;
    this.number -= 1
  &#125;
&#125;</code></pre><p><code>Counter.test.js</code></p><pre><code class="js">import Counter from './Counter'
const counter = new Counter()

test('测试 Counter 中的 addOne 方法', () => &#123;
  counter.addOne()
  expect(counter.number).toBe(1)
&#125;)

test('测试 Counter 中的 minusOne 方法', () => &#123;
  counter.minusOne()
  expect(counter.number).toBe(0)
&#125;)</code></pre><p>运行<code>npm run test</code>:<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039710019" alt title referrerpolicy="no-referrer"></span></p><p>通过第一个测试用例加 1，<code>number</code>的值为 1，当第二个用例减 1 的时候，结果应该是 0。但是这样两个用例间相互干扰不好，可以通过 <code>Jest</code> 的钩子函数来解决。修改测试用例：</p><pre><code class="js">import Counter from "../../../src/utils/Counter";
let counter = null

beforeAll(() => &#123;
  console.log('BeforeAll')
&#125;)

beforeEach(() => &#123;
  console.log('BeforeEach')
  counter = new Counter()
&#125;)

afterEach(() => &#123;
  console.log('AfterEach')
&#125;)

afterAll(() => &#123;
  console.log('AfterAll')
&#125;)

test('测试 Counter 中的 addOne 方法', () => &#123;
  counter.addOne()
  expect(counter.number).toBe(1)
&#125;)
test('测试 Counter 中的 minusOne 方法', () => &#123;
  counter.minusOne()
  expect(counter.number).toBe(-1)
&#125;)</code></pre><p>运行<code>npm run test</code>:<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039710020" alt title referrerpolicy="no-referrer"></span></p><p>可以清晰的看到对应钩子的执行顺序：</p><p><code>beforeAll > (beforeEach > afterEach)(单个用例都会依次执行) > afterAll</code></p><p>除了以上这些基础知识外，其实还有异步代码的测试、Mock、Snapshot 快照测试等，这些我们会在下面 React 的单元测试示例中依次讲解。</p><h3>异步代码的测试</h3><p>众所周知，<code>JS</code>中充满了异步代码。</p><p>正常情况下测试代码是同步执行的，但当我们要测的代码是异步的时候，就会有问题了：<code>test case</code>实际已经结束了，然而我们的异步代码还没有执行，从而导致异步代码没有被测到。</p><p>那怎么办呢？</p><p>对于当前测试代码来说，异步代码什么时候执行它并不知道，因此解决方法很简单。当有异步代码的时候，测试代码跑完同步代码后不立即结束，而是等结束的通知，当异步代码执行完后再告诉<code>jest</code>：“好了，异步代码执行完了，你可以结束任务了”。</p><p><code>jest</code>提供了三种方案来测试异步代码，下面我们分别来看一下。</p><h4>done 关键字</h4><p>当我们的<code>test</code>函数中出现了异步回调函数时，可以给<code>test</code>函数传入一个<code>done</code>参数，它是一个函数类型的参数。如果<code>test</code>函数传入了<code>done</code>，<code>jest</code>就会等到<code>done</code>被调用才会结束当前的<code>test case</code>，如果<code>done</code>没有被调用，则该<code>test</code>自动不通过测试。</p><pre><code class="js">import &#123; fetchData &#125; from './fetchData'
test('fetchData 返回结果为 &#123; success: true &#125;', done => &#123;
  fetchData(data => &#123;
    expect(data).toEqual(&#123;
      success: true
    &#125;)
    done()
  &#125;)
&#125;)</code></pre><p>上面的代码中，我们给<code>test</code>函数传入了<code>done</code>参数，在<code>fetchData</code>的回调函数中调用了<code>done</code>。这样，<code>fetchData</code>的回调中异步执行的测试代码就能够被执行。</p><p>但这里我们思考一种场景：如果使用<code>done</code>来测试回调函数（包含定时器场景，如<code>setTimeout</code>），由于定时器我们设置了 一定的延时（如 3s）后执行，等待 3s 后会发现测试通过了。那假如 <code>setTimeout</code> 设置为几百秒，难道我们也要在 <code>Jest</code> 中等几百秒后再测试吗？</p><p>显然这对于测试的效率是大打折扣的！！</p><p><code>jest</code>中提供了诸如<code>jest.useFakeTimers()</code>、<code>jest.runAllTimers()</code>和<code>toHaveBeenCalledTimes</code>、<code>jest.advanceTimersByTime</code>等<code>api</code>来处理这种场景。</p><blockquote>这里我也不举例详细说明了，有这方面需求的同学可以参考<a href="https://jestjs.io/docs/timer-mocks" rel="nofollow">Timer Mocks</a></blockquote><h4>返回 Promise</h4><blockquote>⚠️ 当对<code>Promise</code>进行测试时，一定要在断言之前加一个<code>return</code>，不然没有等到<code>Promise</code>的返回，测试函数就会结束。可以使用<code>.promises/.rejects</code>对返回的值进行获取，或者使用<code>then/catch</code>方法进行判断。</blockquote><p>如果代码中使用了<code>Promise</code>，则可以通过返回<code>Promise</code>来处理异步代码，<code>jest</code>会等该<code>promise</code>的状态转为<code>resolve</code>时才会结束，如果<code>promise</code>被<code>reject</code>了，则该测试用例不通过。</p><pre><code>// 假设 user.getUserById（参数id） 返回一个promise
it('测试promise成功的情况', () => &#123;
  expect.assertions(1);
  return user.getUserById(4).then((data) => &#123;
    expect(data).toEqual('Cosen');
  &#125;);
&#125;);
it('测试promise错误的情况', () => &#123;
  expect.assertions(1);
  return user.getUserById(2).catch((e) => &#123;
    expect(e).toEqual(&#123;
      error: 'id为2的用户不存在',
    &#125;);
  &#125;);
&#125;);
</code></pre><p>注意，上面的第二个测试用例可用于测试<code>promise</code>返回<code>reject</code>的情况。这里用<code>.catch</code>来捕获<code>promise</code>返回的<code>reject</code>，当<code>promise</code>返回<code>reject</code>时，才会执行<code>expect</code>语句。而这里的<code>expect.assertions(1)</code>用于确保该测试用例中有一个<code>expect</code>被执行了。</p><p>对于<code>Promise</code>的情况，<code>jest</code>还提供了一对匹配符<code>resolves/rejects</code>，其实只是上面写法的语法糖。上面的代码用匹配符可以改写为：</p><pre><code class="js">// 使用'.resolves'来测试promise成功时返回的值
it('使用'.resolves'来测试promise成功的情况', () => &#123;
  return expect(user.getUserById(4)).resolves.toEqual('Cosen');
&#125;);
// 使用'.rejects'来测试promise失败时返回的值
it('使用'.rejects'来测试promise失败的情况', () => &#123;
  expect.assertions(1);
  return expect(user.getUserById(2)).rejects.toEqual(&#123;
    error: 'id为2的用户不存在',
  &#125;);
&#125;);</code></pre><h4>async/await</h4><p>我们知道<code>async/await</code>其实是<code>Promise</code>的语法糖，可以更优雅地写异步代码，<code>jest</code>中也支持这种语法。</p><p>我们把上面的代码改写一下：</p><pre><code class="js">// 使用async/await来测试resolve
it('async/await来测试resolve', async () => &#123;
  expect.assertions(1);
  const data = await user.getUserById(4);
  return expect(data).toEqual('Cosen');
&#125;);
// 使用async/await来测试reject
it('async/await来测试reject', async () => &#123;
  expect.assertions(1);
  try &#123;
    await user.getUserById(2);
  &#125; catch (e) &#123;
    expect(e).toEqual(&#123;
      error: 'id为2的用户不存在',
    &#125;);
  &#125;
&#125;);</code></pre><blockquote>⚠️ 使用<code>async</code>不用进行<code>return</code>返回，并且要使用<code>try/catch</code>来对异常进行捕获。</blockquote><h3><code>Mock</code></h3><p>介绍<code>jest</code>中的<code>mock</code>之前，我们先来思考一个问题：为什么要使用<code>mock</code>函数？</p><p>在项目中，一个模块的方法内常常会去调用另外一个模块的方法。在单元测试中，我们可能并不需要关心内部调用的方法的执行过程和结果，只想知道它是否被正确调用即可，甚至会指定该函数的返回值。这个时候，<code>mock</code>的意义就很大了。</p><p><code>jest</code>中与<code>mock</code>相关的<code>api</code>主要有三个，分别是<code>jest.fn()</code>、<code>jest.mock()</code>、<code>jest.spyOn()</code>。使用它们创建<code>mock</code>函数能够帮助我们更好的测试项目中一些逻辑较复杂的代码。我们在测试中也主要是用到了<code>mock</code>函数提供的以下三种特性：</p><ul><li>捕获函数调用情况</li><li>设置函数返回值</li><li>改变函数的内部实现</li></ul><p>下面，我将分别介绍这三种方法以及他们在实际测试中的应用。</p><h4><code>jest.fn()</code></h4><p><code>jest.fn()</code>是创建<code>mock</code>函数最简单的方式，如果没有定义函数内部的实现，<code>jest.fn()</code>会返回<code>undefined</code>作为返回值。</p><pre><code class="js">// functions.test.js

test('测试jest.fn()调用', () => &#123;
  let mockFn = jest.fn();
  let res = mockFn('厦门','青岛','三亚');

  // 断言mockFn的执行后返回undefined
  expect(res).toBeUndefined();
  // 断言mockFn被调用
  expect(mockFn).toBeCalled();
  // 断言mockFn被调用了一次
  expect(mockFn).toBeCalledTimes(1);
  // 断言mockFn传入的参数为1, 2, 3
  expect(mockFn).toHaveBeenCalledWith('厦门','青岛','三亚');
&#125;)</code></pre><p><code>jest.fn()</code>所创建的<code>mock</code>函数还可以设置返回值，定义<code>内部实现</code>或<code>返回Promise对象</code>。</p><pre><code class="js">// functions.test.js

test('测试jest.fn()返回固定值', () => &#123;
  let mockFn = jest.fn().mockReturnValue('default');
  // 断言mockFn执行后返回值为default
  expect(mockFn()).toBe('default');
&#125;)

test('测试jest.fn()内部实现', () => &#123;
  let mockFn = jest.fn((num1, num2) => &#123;
    return num1 + num2;
  &#125;)
  // 断言mockFn执行后返回20
  expect(mockFn(10, 10)).toBe(20);
&#125;)

test('测试jest.fn()返回Promise', async () => &#123;
  let mockFn = jest.fn().mockResolvedValue('default');
  let res = await mockFn();
  // 断言mockFn通过await关键字执行后返回值为default
  expect(res).toBe('default');
  // 断言mockFn调用后返回的是Promise对象
  expect(Object.prototype.toString.call(mockFn())).toBe("[object Promise]");
&#125;)</code></pre><h4><code>jest.mock()</code></h4><p>一般在真实的项目里，测试异步函数的时候，不会真正的发送 <code>ajax</code> 请求去请求这个接口，为什么？</p><p>比如有 <code>1w</code> 个接口要测试，每个接口要 <code>3s</code> 才能返回，测试全部接口需要 <code>30000s</code>，那么这个自动化测试的时间就太慢了</p><p>我们作为前端只需要去确认这个异步请求发送成功就好了，至于后端接口返回什么内容我们就不测了，这是后端自动化测试要做的事情。</p><p>这里以一个<code>axios请求</code>的<code>demo</code>为例来说明：</p><pre><code class="js">// user.js
import axios from 'axios'

export const getUserList = () => &#123;
  return axios.get('/users').then(res => res.data)
&#125;
</code></pre><p>对应测试文件<code>user.test.js</code>:</p><pre><code class="js">import &#123; getUserList &#125; from '@/services/user.js'
import axios from 'axios'
// 👇👇
jest.mock('axios')
// 👆👆
test.only('测试 getUserList', async () => &#123;
  axios.get.mockResolvedValue(&#123; data: ['Cosen','森林','柯森'] &#125;)
  await getUserList().then(data => &#123;
    expect(data).toBe(['Cosen','森林','柯森'])
  &#125;)
&#125;)</code></pre><p>我们在测试用例的最上面加入了<code>jest.mock('axios')</code>，我们让<code>jest</code>去对<code>axios</code>做模拟，这样就不会去请求真正的数据了。然后调用<code>axios.get</code>的时候，不会真实的请求这个接口，而是会以我们写的<code>&#123; data: ['Cosen','森林','柯森'] &#125;</code>去模拟请求成功后的结果。</p><blockquote>当然模拟异步请求是需要时间的，如果请求多的话时间就很长，这时候可以在本地<code>mock</code>数据，在根目录下新建 <code>__mocks__</code>文件夹。这种方式就不用去模拟<code>axios</code>，而是直接走的本地的模拟方法，也是比较常用的一种方式，这里就不展开说明了。</blockquote><h4><code>jest.spyOn()</code></h4><p><code>jest.spyOn()</code>方法同样创建一个<code>mock</code>函数，但是该<code>mock</code>函数不仅能够捕获函数的调用情况，还可以正常的执行被<code>spy</code>的函数。实际上，<code>jest.spyOn()</code>是<code>jest.fn()</code>的语法糖，它创建了一个和被<code>spy</code>的函数具有相同内部代码的<code>mock函数</code>。</p><h3>Snapshot 快照测试</h3><p>所谓<code>snapshot</code>，即快照也。通常涉及 UI 的自动化测试，思路是把某一时刻的标准状态拍个快照。</p><pre><code class="js">describe("xxx页面", () => &#123;
  // beforeEach(() => &#123;
  //   jest.resetAllMocks()
  // &#125;)
  // 使用 snapshot 进行 UI 测试
  it("页面应能正常渲染", () => &#123;
    const wrapper = wrappedShallow()
    expect(wrapper).toMatchSnapshot()
  &#125;)
&#125;)</code></pre><p>当使用<code>toMatchSnapshot</code>的时候，<code>Jest</code> 将会渲染组件并创建其快照文件。这个快照文件包含渲染后组件的整个结构，并且应该与测试文件本身一起提交到代码库。当我们再次运行快照测试时，<code>Jest</code> 会将新的快照与旧的快照进行比较，如果两者不一致，测试就会失败，从而帮助我们确保用户界面不会发生意外改变。</p><h2>🎯 总结</h2><p>到这里，关于前端单元测试的一些基础背景和<code>Jest</code>的基础<code>api</code>就介绍完了，在下一篇文章中，我会结合项目中的一个<code>React组件</code>来讲解如何做<code>组件单元测试</code>。</p><h2>📜 参考链接</h2><ul><li><a href="https://segmentfault.com/a/1190000016717356">https://segmentfault.com/a/11...</a></li></ul>  
</div>
            