"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[549],{3905:(e,t,n)=>{n.d(t,{Zo:()=>p,kt:()=>f});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function s(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?s(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):s(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},s=Object.keys(e);for(r=0;r<s.length;r++)n=s[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(r=0;r<s.length;r++)n=s[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var c=r.createContext({}),i=function(e){var t=r.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):o(o({},t),e)),n},p=function(e){var t=i(e.components);return r.createElement(c.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},d=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,s=e.originalType,c=e.parentName,p=l(e,["components","mdxType","originalType","parentName"]),d=i(n),f=a,m=d["".concat(c,".").concat(f)]||d[f]||u[f]||s;return n?r.createElement(m,o(o({ref:t},p),{},{components:n})):r.createElement(m,o({ref:t},p))}));function f(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var s=n.length,o=new Array(s);o[0]=d;var l={};for(var c in t)hasOwnProperty.call(t,c)&&(l[c]=t[c]);l.originalType=e,l.mdxType="string"==typeof e?e:a,o[1]=l;for(var i=2;i<s;i++)o[i]=n[i];return r.createElement.apply(null,o)}return r.createElement.apply(null,n)}d.displayName="MDXCreateElement"},543:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>c,contentTitle:()=>o,default:()=>u,frontMatter:()=>s,metadata:()=>l,toc:()=>i});var r=n(7462),a=(n(7294),n(3905));const s={title:"Delete testcases of task",sidebar_position:4},o=void 0,l={unversionedId:"usage/tc/delete",id:"usage/tc/delete",title:"Delete testcases of task",description:"You can delete testcases related to the task using the cppt tc delete command.",source:"@site/docs/usage/tc/delete.md",sourceDirName:"usage/tc",slug:"/usage/tc/delete",permalink:"/CPPT/docs/usage/tc/delete",draft:!1,editUrl:"https://github.com/vishalagrawal22/CPPT/tree/main/website/docs/usage/tc/delete.md",tags:[],version:"current",sidebarPosition:4,frontMatter:{title:"Delete testcases of task",sidebar_position:4},sidebar:"tutorialSidebar",previous:{title:"Edit testcases of task",permalink:"/CPPT/docs/usage/tc/edit"},next:{title:"Stress test task",permalink:"/CPPT/docs/usage/test"}},c={},i=[{value:"Usage",id:"usage",level:2},{value:"Demo",id:"demo",level:2}],p={toc:i};function u(e){let{components:t,...s}=e;return(0,a.kt)("wrapper",(0,r.Z)({},p,s,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("p",null,"You can delete testcases related to the task using the ",(0,a.kt)("inlineCode",{parentName:"p"},"cppt tc delete")," command."),(0,a.kt)("p",null,"It accepts a list of space-separated testcase numbers, deletes all those testcase, and reorders the remaining testcases."),(0,a.kt)("p",null,"Unlike other tc commands, if you do not specify the ",(0,a.kt)("inlineCode",{parentName:"p"},"TCS")," argument, the delete command fails purposely to prevent you from deleting all testcases by mistake (if you want to delete all testcases, you could enter 0 instead)."),(0,a.kt)("h2",{id:"usage"},"Usage"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-shell"},"cppt tc delete --help\n")),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-shell"},"Usage: cppt tc delete [OPTIONS] FILENAME TCS...\n\n  Delete a set of testcases related to FILENAME\n\n  Args:\n\n  FILENAME of the source code file with file extension\n  TCS: space seperated list of test case numbers (0 for all)\n\nOptions:\n  -p, --path DIRECTORY  path to the folder which contains the souce code\n  -h, --help            Show this message and exit.\n")),(0,a.kt)("h2",{id:"demo"},"Demo"),(0,a.kt)("p",null,(0,a.kt)("img",{alt:"Testcase delete command demo",src:n(6006).Z,width:"1920",height:"1080"})))}u.isMDXComponent=!0},6006:(e,t,n)=>{n.d(t,{Z:()=>r});const r=n.p+"assets/images/tc-delete-6e79fc2a7c6e806fac046395ff9b67e5.gif"}}]);