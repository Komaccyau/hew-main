let width = 720    // We will scale the photo width to this
let height = 0     // This will be computed based on the input stream

let streaming = false

let video = null
let canvas = null
let photo = null
let startbutton = null
let constrains = { video: true, audio: true }
let recorder = null
let record_data = []

/**
 * ユーザーのデバイスによるカメラ表示を開始し、
 * 各ボタンの挙動を設定する
 *
 */
function startup() {
  video = document.getElementById('video')
  canvas = document.getElementById('canvas')
  photo = document.getElementById('photo')
  startbutton = document.getElementById('startbutton')
  stopbutton = document.getElementById('stopbutton')
  rec = document.getElementById('rec')
  result_video = document.getElementById('result_video')
  check_text = document.getElementById('check_text')
  ok = document.getElementById('ok')
  ng = document.getElementById('ng')
  next = document.getElementById('next')
  loading = document.getElementById('loading')
  leftside = document.getElementById('leftside')

  videoStart()

  video.addEventListener('canplay', function (ev) {
    if (!streaming) {
      height = video.videoHeight / (video.videoWidth / width)
      video.setAttribute('width', width)
      video.setAttribute('height', height)
      streaming = true
    }
  }, false)

  startRecorder()

  // 「start」ボタンを押したときの処理
  startbutton.addEventListener('click', function (ev) {
    recorder.start()
    ev.preventDefault()
    document.getElementById('btn_audio').play(); // 音を再生
    startbutton.style.display = "none"
    stopbutton.style.display = "flex"
    rec.style.display = "block"
  }, false);

  // 「stop」ボタンを押したときの処理
  stopbutton.addEventListener('click', function (ev) {
    recorder.stop()
    document.getElementById('btn_audio').pause(); // 音を停止
    video.style.display = "none"
    result_video.style.display = "block"
    stopbutton.style.display = "none"
    rec.style.display = "none"
  })

  // 「ok」ボタンを押したときの処理
  ok.addEventListener('click', function (ev) {
    console.log(record_data)
    var blob = new Blob(record_data, { type: 'video/webm' })
    var url = window.URL.createObjectURL(blob)
    var a = document.createElement('a')
    document.body.appendChild(a)
    a.style = 'display:none'
    a.href = url;
    a.download = 'video.webm'
    a.click()
    window.URL.revokeObjectURL(url)
    next.style.display = "flex"
    check_text.style.display = "none"
    ok.style.display = "none"
    ng.style.display = "none"
    leftside.style.display = "none"
  })

  // 「next」ボタンを押したときの処理
  next.addEventListener('click', function (ev) {
    loading.style.display = "block"
  })
}

// カメラ映像を写す処理
function videoStart() {
  streaming = false
  console.log(streaming)
  navigator.mediaDevices.getUserMedia(constrains)
    .then(function (stream) {
      video.srcObject = stream
      video.play()
    })
    .catch(function (err) {
      console.log("An error occured! " + err)
    })
}

// 録画処理（コメント部分デバッグ用）
function startRecorder() {
  navigator.mediaDevices.getUserMedia(constrains)
    .then(function (stream) {
      recorder = new MediaRecorder(stream)
      recorder.ondataavailable = function (e) {
        var testvideo = document.getElementById('test')
        testvideo.setAttribute('controls', '')
        testvideo.setAttribute('width', width)
        testvideo.setAttribute('height', height)
        var outputdata = window.URL.createObjectURL(e.data)
        record_data.push(e.data)
        testvideo.src = outputdata
      }
    })
}

startup()