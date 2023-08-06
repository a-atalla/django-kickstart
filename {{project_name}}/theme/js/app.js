import { Application } from "@hotwired/stimulus"

import HelloController from "./controllers/hello"

window.Stimulus = Application.start()

window.Stimulus.register("hello", HelloController)
