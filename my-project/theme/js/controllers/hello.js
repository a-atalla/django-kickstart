import { Controller } from "@hotwired/stimulus"

enum Direction {
    RIGHT="RIGHT",
    LEFT="LEFT",
}

export default class extends Controller {
    connect() {
        console.log(Direction.RIGHT)
        console.log("Hello, Stimulus!", this.element)
    }
}